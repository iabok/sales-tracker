'''
 Stations routing configurations
'''
from django.conf.urls import url
from stations.views import StationCreate, StationUpdate, StationDelete

urlpatterns = [
    # ...
    url(r'station/$', StationCreate.as_view(), name='station-add'),
    url(r'station/add/$', StationCreate.as_view(), name='station-add'),
    url(r'station/edit/(?P<pk>[0-9]+)/$', StationUpdate.as_view(), name='station-update'),
    url(r'station/delete/(?P<pk>[0-9]+)/delete/$', StationDelete.as_view(), name='station-delete'),
]
