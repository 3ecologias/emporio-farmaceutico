from oscar.apps.basket.views import BasketView as CoreBasketView
from recifegrafica.arts_and_orders.models import UploadForm

##DEFAULT IMPORTS##
import json

from django import shortcuts
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView, View
from extra_views import ModelFormSetView

from oscar.apps.basket import signals
from oscar.core import ajax
from oscar.core.loading import get_class, get_classes, get_model
from oscar.core.utils import redirect_to_referrer, safe_referrer

Applicator = get_class('offer.utils', 'Applicator')
(BasketLineFormSet, BasketLineForm, AddToBasketForm, BasketVoucherForm,
 SavedLineFormSet, SavedLineForm) \
    = get_classes('basket.forms', ('BasketLineFormSet', 'BasketLineForm',
                                   'AddToBasketForm', 'BasketVoucherForm',
                                   'SavedLineFormSet', 'SavedLineForm'))
Repository = get_class('shipping.repository', ('Repository'))
OrderTotalCalculator = get_class(
    'checkout.calculators', 'OrderTotalCalculator')
BasketMessageGenerator = get_class('basket.utils', 'BasketMessageGenerator')

####################

class BasketView(CoreBasketView):


    def formset_valid(self, formset):
        if 'upload_file' in self.request.POST:
            files = self.request.FILES
            for form in formset:
                if form.is_valid():
                    line = form.instance
                    self.request.line = get_model('basket', 'Line').objects.get(basket=self.request.basket, product=line.product.pk)
                    self.request.line.art_file = form.instance.art_file
                    self.request.line.save()

        return super(BasketView, self).formset_valid(formset)

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)

        context["upload_form"] = UploadForm

        return context
