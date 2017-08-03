'''
 Funds views
'''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
# from el_pagination.views import AjaxListView
from funds.models import Bank, Wallet


class BankList(ListView):
    '''
     Updates Banks
    '''
    model = Bank
    context_object_name = 'funds'
    template_name = '../templates/bank_list.html'


class BankUpdate(UpdateView):
    '''
     Updates Banks
    '''
    model = Bank
    template_name = '../templates/bank_update.html'
    fields = ['amount']


class WalletTop(CreateView):
    '''
     Transfer money stations
    '''
    model = Wallet
    fields = '__all__'
    template_name = '../templates/wallet_top.html'
