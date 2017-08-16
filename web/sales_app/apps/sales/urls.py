'''
 funds routing configurations
'''
from django.conf.urls import url
from .views import SalesFormView

urlpatterns = [
    url(r'sales/add$', SalesFormView.as_view(), name='sales-add'),
]
