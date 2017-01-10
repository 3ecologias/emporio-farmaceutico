from oscar.apps.shipping import repository
from decimal import Decimal as D
from oscar.apps.shipping.methods import Free, FixedPrice, NoShippingRequired
from oscar.apps.shipping.repository import Repository as CoreRepository
from oscar.apps.shipping import methods, models
from oscar.apps.shipping.models import WeightBased
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

class HandDelivery(methods.FixedPrice):

    code = "hand-delivery"
    name = _("Entrega Expressa")
    charge_excl_tax = D('0.00')
    charge_incl_tax = D('15.00')

class Repository(CoreRepository):

    methods = [HandDelivery()] # init shipping method to default hand delivery

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):

    # check if shipping method(s) is available for shipping country (for instance 'BR')

        if shipping_addr :

            # retrieve shipping method(s) for shipping country

            weightbased_set = WeightBased.objects.all().filter(countries=shipping_addr.country.code)

            # set shipping method(s) if available for shipping country

            if weightbased_set :

                methods = list(weightbased_set)

                methods += [HandDelivery()]

            else :

                # no shipping method is available for shipping country, error message will be displayed by core

                methods = []
                # no shipping address, set shipping method to default hand delivery

        else :

            methods = [HandDelivery()]


        return methods
