from django.conf.urls import url
from stations.views import StationView, StationCreate, StationUpdate, StationDelete

urlpatterns = [
    # ...
    url(r'station/$', StationView.as_view(), name='station'),
    url(r'station/add/$', StationCreate.as_view(), name='station-add'),
    url(r'station/(?P<pk>[0-9]+)/$', StationUpdate.as_view(), name='station-update'),
    url(r'station/(?P<pk>[0-9]+)/delete/$', StationDelete.as_view(), name='station-delete'),
]
