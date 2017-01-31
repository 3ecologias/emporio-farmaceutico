from django.shortcuts import render
from django.views import generic
from recifegrafica.arts_and_orders.models import Document

# Create your views here.
class ArtListView(generic.ListView):
    model = Document
    context_object_name = 'files'
    template_name = 'dash_custom/arts.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArtListView, self).get_context_data(**kwargs)
        ctx['files'] = Document.objects.all()
        
        return ctx
