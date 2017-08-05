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
    stations = forms.ModelMultipleChoiceField(queryset=Station.objects.all())
    date = forms.CharField(required=True)
    petrol_open = forms.CharField(required=True)
    petrol_close = forms.CharField(required=True)
    petrol_price = forms.CharField(required=True)
    desiel_open = forms.CharField(required=True)
    desiel_close = forms.CharField(required=True)
    desiel_price = forms.CharField(required=True)
    product_name = forms.ModelMultipleChoiceField(queryset=Product.objects.values_list('name'))
    quantity = forms.CharField()
    price = forms.CharField()
    credit_name = forms.CharField()
    amount = forms.CharField()
