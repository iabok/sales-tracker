from django.conf.urls import url
from stations.views import StationCreate, StationUpdate, StationDelete

urlpatterns = [
    # ...
    url(r'station/add/$', StationCreate.as_view(), name='station-add'),
    url(r'station/(?P<pk>[0-9]+)/$', StationUpdate.as_view(), name='station-update'),
    url(r'station/(?P<pk>[0-9]+)/delete/$', StationDelete.as_view(), name='station-delete'),
]