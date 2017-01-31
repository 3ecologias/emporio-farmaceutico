
"""recifegrafica URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static
from recifegrafica.arts_and_orders import views as artsview
from recifegrafica.arts_and_orders.dashboard.app import application as arts_list_app


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # django admin is not officially supported by oscar - you should use the dashboard instead
    url(r'^admin/', include(admin.site.urls)),

    #custom urls
    url(r'^basket/configure_arts/', artsview.simple_upload),
    url(r'^dashboard/arts_list/', include(arts_list_app.urls)),
    #oscar core urls
    url(r'', include(application.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
