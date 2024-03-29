from django.conf import settings
from decimal import Decimal

from oscar.apps.payment import exceptions
from oscar.core import prices
from django.http import HttpResponseRedirect

from cielo import (
    PaymentAttempt,
    GetAuthorizedException,
    CaptureException,
)

from .forms import (
    CieloForm,
    HiddenCieloForm,
)


class CieloPaymentDetailsMixin(object):
    cielo_form_class = CieloForm
    cielo_hidden_form_class = HiddenCieloForm

    def get_cielo_form_class(self):
        return self.cielo_form_class

    def get_cielo_hidden_form_class(self):
        return self.cielo_hidden_form_class

    def get_cielo_credentials(self):
        return {
            'affiliation_id': getattr(settings, 'OSCAR_CIELO_NUMERO', ''),
            'api_key': getattr(settings, 'OSCAR_CIELO_CHAVE', ''),
        }

    def get_cielo_payment_data(self, order_number, total_incl_tax, form_data):
        installments = int(form_data.get('installments'))

        if installments == 1:
            transaction = PaymentAttempt.CASH
        else:
            transaction = PaymentAttempt.INSTALLMENT_STORE

        data = {
            'sandbox': getattr(settings, 'OSCAR_CIELO_SANDBOX', ''),
            'card_type': form_data.get('card_type'),
            'card_number': form_data.get('number'),
            'cvc2': form_data.get('ccv'),
            'exp_month': form_data.get('expiry_month').month,
            'exp_year': form_data.get('expiry_month').year,
            'card_holders_name': form_data.get('name'),
            'total': total_incl_tax,
            'order_id': order_number,
            'transaction': transaction,
            'installments': installments,
        }

        data.update(self.get_cielo_credentials())

        return data

    def get_cielo_order_total(self):
        shipping_address = self.get_shipping_address(self.request.basket)
        shipping_method = self.get_shipping_method(
            self.request.basket, shipping_address)
        shipping_charge = shipping_method.calculate(self.request.basket)

        total_incl_tax = self.get_order_totals(
            self.request.basket, shipping_charge).incl_tax

        return total_incl_tax

    def get_cielo_form(self):
        order_total = self.get_cielo_order_total()

        action = self.request.POST.get('action')

        if action in ('place_order', 'change_details'):
            """ When placing an order or going to change details
            The values of the hidden form is passed to a visible form
            """
            hidden_form = self.get_cielo_hidden_form_class()(
                order_total, self.request.POST)

            if hidden_form.is_valid():
                return self.get_cielo_form_from_hidden(hidden_form)

        if self.request.method == 'POST':
            return self.get_cielo_form_class()(order_total, self.request.POST)

        return self.get_cielo_form_class()(order_total)

    def get_cielo_hidden_form(self, form):
        """ Creates a HiddenCieloForm from a CieloForm.
        Including the values in cleaned_data.
        """
        hidden_form_initial = {}

        for field in form.cleaned_data:
            val = form.cleaned_data.get(field)
            hidden_form_initial[field] = val

        hidden_form = self.get_cielo_hidden_form_class()(form._order_total,
            initial=hidden_form_initial)

        return hidden_form

    def get_cielo_form_from_hidden(self, hidden_form):
        expiration = hidden_form.cleaned_data.get('expiry_month')

        data = hidden_form.data.dict()
        data.pop('expiry_month')

        data['expiry_month_0'] = "%02d" % (expiration.month)
        data['expiry_month_1'] = "%04d" % (expiration.year)

        return self.get_cielo_form_class()(hidden_form._order_total, data)

    def get_cielo_context_data(self, **kwargs):
        context = {}

        form = self.get_cielo_form()

        if self.preview:
            """ At this point all data needed was already
            filled by the user.
            """
            # Populate cleaned_data
            form.is_valid()

            # Render a hidden form with populated data
            context['cielo_hidden_form'] = self.get_cielo_hidden_form(form)

            # Extra context to go in preview
            form_data = form.cleaned_data

            order_total = form._order_total
            order_installments = int(form_data.get('installments'))

            # Applying interest

            # if order_installments<4:
            #     order_total += (order_total * Decimal(0.0325))
            # elif order_installments<7:
            #     order_total += (order_total * Decimal(0.0350))
            # else:
            #     order_total += (order_total * Decimal(0.0400))
            #
            order_installment_value = order_total / order_installments

            order_card_type_label =\
                dict(form.fields['card_type'].choices)[
                    form_data.get('card_type')]

            context['cielo_data_card_type'] = form_data.get('card_type')
            context['cielo_data_card_type_label'] = order_card_type_label
            context['cielo_data_installment_value'] = order_installment_value
            context['cielo_data_installments'] = order_installments
            context['cielo_data_holders_name'] = form_data.get('name')
            context['cielo_data_card_number'] = form_data.get('number')
            context['cielo_data_expiration'] = form_data.get('expiry_month')
            context['cielo_data_security_code'] = form_data.get('ccv')

        else:
            context['cielo_form'] = form

        return context

    def handle_cielo_post(self, *args, **kwargs):
        action = self.request.POST.get('action')

        if action == 'change_details':
            """ When user choose to change details.
            Eg.: credit card number, name, etc...
            """
            self.preview = False

        elif action != 'place_order':
            """ Go to preview when user save his details
            with success.
            """
            self.preview = self.get_cielo_form().is_valid()


    def capture_cielo_payment(self, order_number, total_incl_tax):
        form = self.get_cielo_form()

        if not form.is_valid():
            """ Something wrong with the submitted values
            Maybe some value was changed before submiting
            """
            raise
        #APLYING INTEREST#
        form_data = form.cleaned_data
        order_installments = int(form_data.get('installments'))

        # if order_installments<4:
        #     total_incl_tax.incl_tax += (total_incl_tax.incl_tax * Decimal(0.0325))
        # elif order_installments<7:
        #     total_incl_tax.incl_tax += (total_incl_tax.incl_tax * Decimal(0.0350))
        # else:
        #     total_incl_tax.incl_tax += (total_incl_tax.incl_tax * Decimal(0.0400))

        attempt = self.get_cielo_payment_data(
            order_number, total_incl_tax, form.cleaned_data)

        attempt['total'] = attempt['total'].incl_tax
        attempt_cielo = PaymentAttempt(**attempt)

        try:
            attempt_cielo.get_authorized()
            attempt_cielo.capture()
            print "pass"
        except (GetAuthorizedException, CaptureException), e:
            print "except"
            raise exceptions.UnableToTakePayment(unicode(e))

        return attempt
