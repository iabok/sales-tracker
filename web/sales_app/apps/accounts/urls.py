from django.conf.urls import url
from accounts.views import AccountsFormView

urlpatterns = [
    url(r'^accounts/add/$', AccountsFormView.as_view(), name='signup'),
]
