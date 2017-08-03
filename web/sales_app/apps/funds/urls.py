'''
 funds routing configurations
'''
from django.conf.urls import url
from funds.views import BankList, BankUpdate, WalletTop

urlpatterns = [
    url(r'funds/$', BankList.as_view(), name='bank-list'),
    url(r'funds/update/(?P<pk>[0-9]+)/$', BankUpdate.as_view(), \
        name='bank-update'),
    url(r'funds/transfer/$', WalletTop.as_view(), name='Wallet-top'),
    # url(r'funds/details/$', BankDetails.as_view(), name='bank-list'),
]
