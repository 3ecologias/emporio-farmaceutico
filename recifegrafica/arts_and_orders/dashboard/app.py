from django.conf.urls import patterns, url
from django.contrib.admin.views.decorators import staff_member_required
from oscar.core.application import Application

from recifegrafica.arts_and_orders.dashboard import views


class ArtsDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    art_list_view = views.ArtListView

    def get_urls(self):
        urlpatterns = [
            url(r'^$',
                self.art_list_view.as_view(),
                name='arts-list'),
        ]
        return self.post_process_urls(urlpatterns)


application = ArtsDashboardApplication()
