'''
 Stations routing configurations
'''
from django.conf.urls import url
from stations.views import StationCreate, StationUpdate, StationDelete, \
                           StationDetail

urlpatterns = [
    # ...
    url(r'station/$', StationCreate.as_view(), name='station-add'),
    url(r'station/add/$', StationCreate.as_view(), name='station-add'),
    url(r'station/view/(?P<pk>[0-9]+)/$', StationDetail.as_view(), \
        name='station-details'),
    url(r'station/edit/(?P<pk>[0-9]+)/$', StationUpdate.as_view(), \
        name='station-update'),
    url(r'station/(?P<pk>[0-9]+)/delete/$', StationDelete.as_view(), \
        name='station-delete')
]
