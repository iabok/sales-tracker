from django.conf.urls import url
from accounts.views import AccountsFormView, accountsList

urlpatterns = [
    url(r'^accounts/$', accountsList.as_view(), name='account-list'),
    url(r'^accounts/add/$', AccountsFormView.as_view(), name='signup'),
]
