from oscar.apps.basket.views import BasketView as CoreBasketView
from recifegrafica.arts_and_orders.models import UploadForm

class BasketView(CoreBasketView):

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)

        context["upload_form"] = UploadForm

        return context
