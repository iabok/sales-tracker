'''
  Sales Add Form
'''
from django import forms
from stations.models import Station
from products.models import Product


class SalesForm(forms.Form):
    '''
     Sales Form
    '''
    stations_list = Station.objects.values_list('id', 'name')
    product_list = Product.objects.values_list('id', 'name')

    station = forms.ChoiceField(choices=stations_list, required=True)
    date = forms.CharField(required=True)
    petrol_open = forms.CharField(required=True)
    petrol_close = forms.CharField(required=True)
    petrol_price = forms.CharField(required=True)
    desiel_open = forms.CharField(required=True)
    desiel_close = forms.CharField(required=True)
    desiel_price = forms.CharField(required=True)
    product_name = forms.ChoiceField(choices=product_list, required=False)
    quantity = forms.CharField(required=False)
    price = forms.CharField(required=False)
    credit_name = forms.CharField(required=False)
    amount = forms.CharField(required=False)
