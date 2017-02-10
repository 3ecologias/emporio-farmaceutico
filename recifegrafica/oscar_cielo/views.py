from django.conf import settings

from oscar.apps.payment.models import SourceType, Source
from oscar.apps.checkout.views import PaymentDetailsView as BasePaymentDetailsView
from django.shortcuts import render

from recifegrafica.oscar_cielo.mixins import CieloPaymentDetailsMixin


class CieloPaymentDetailsView(BasePaymentDetailsView,
                              CieloPaymentDetailsMixin):

    PROCESSED_STATUS = getattr(settings, 'OSCAR_CIELO_PROCESSED_STATUS',
                                         'Processado')

    def get_context_data(self, **kwargs):
        context = super(CieloPaymentDetailsView, self).get_context_data(
            **kwargs)
        context.update(self.get_cielo_context_data())

        return context

    def post(self, request, *args, **kwargs):
        # Posting to payment-details isn't the right thing to do.  Form
        # submissions should use the preview URL.
        self.handle_cielo_post(*args, **kwargs)
        context = self.get_context_data()
        if not self.preview:
            return render(request, 'checkout/payment_details.html', context)

        # We use a custom parameter to indicate if this is an attempt to place
        # an order (normally from the preview page).  Without this, we assume a
        # payment form is being submitted from the payment details view. In
        # this case, the form needs validating and the order preview shown.
        if request.POST.get('action', '') == 'place_order':
            return self.handle_place_order_submission(request)
        return self.handle_payment_details_submission(request)

    def handle_payment(self, order_number, total_incl_tax, **kwargs):
        attempt = self.capture_cielo_payment(order_number, total_incl_tax)

        transaction_id = attempt['transaction']

        source_type, _ = SourceType.objects.get_or_create(name='Cielo')

        total_incl_tax = total_incl_tax.incl_tax

        source = Source(
            source_type=source_type,
            currency='BRL',
            amount_allocated=total_incl_tax,
            amount_debited=total_incl_tax,
            reference=transaction_id,
        )

        self.add_payment_source(source)


    def place_order(self, *args, **kwargs):

        order = super(CieloPaymentDetailsView, self).place_order(*args,
                                                                 **kwargs)
        order.set_status(self.PROCESSED_STATUS)

        return order
