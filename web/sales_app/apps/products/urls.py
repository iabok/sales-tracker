'''
 Products routing configurations
'''
from django.conf.urls import url
from products.views import ProductCreate, ProductUpdate, ProductDelete, \
                            ProductList, ProductDetail

urlpatterns = [
    # ...
    url(r'product/$', ProductList.as_view(), name='product-list'),
    url(r'product/add/$', ProductCreate.as_view(), name='product-add'),
    url(r'product/view/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), \
        name='product-details'),
    url(r'product/edit/(?P<pk>[0-9]+)/$', ProductUpdate.as_view(), \
        name='product-update'),
    url(r'product/(?P<pk>[0-9]+)/delete/$', ProductDelete.as_view(), \
        name='product-delete')
]
