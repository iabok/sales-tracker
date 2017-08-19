'''
 funds routing configurations
'''
from django.conf.urls import url
from .views import SalesFormView, SalesList, SalesDetail

urlpatterns = [
    url(r'sales/$', SalesList.as_view(), name='sales-list'),
    url(r'sales/add$', SalesFormView.as_view(), name='sales-add'),
    url(r'sales/view/(?P<pk>[0-9]+)/$', SalesDetail.as_view(),
        name='sales-details'),
    # url(r'station/edit/(?P<pk>[0-9]+)/$', StationUpdate.as_view(), \
    #     name='station-update'),
    # url(r'station/(?P<pk>[0-9]+)/delete/$', StationDelete.as_view(), \
    #     name='station-delete')
]
