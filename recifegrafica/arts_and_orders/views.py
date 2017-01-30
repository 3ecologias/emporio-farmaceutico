from django.shortcuts import render, HttpResponseRedirect, redirect
from recifegrafica.arts_and_orders.models import UploadForm
from django.conf import settings
from django.contrib.auth.models import User

def simple_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = None
            if request.user.is_authenticated():
                user = request.user
            document = form.cleaned_data['document']
            product_description = request.POST.get('product_title','')
            form.product_description = product_description
            art = form.save(commit=False)
            art.user = user
            art.save()
            return redirect('/basket')
    else:
        form = UploadForm()
    return HttpResponseRedirect('/basket')
