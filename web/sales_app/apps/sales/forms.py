'''
  Sales Add Form
'''
from django import forms
from stations.models import Station
from productSalesTotal.models import Product


class SalesForm(forms.Form):
    '''
     Sales Form
    '''
    stations = forms.ModelMultipleChoiceField(queryset=Station.objects.all())
    date = forms.CharField(required=True)
    petrol_opening = forms.CharField(required=True)
    petrol_closing = forms.CharField(required=True)
    petrol_price = forms.CharField(required=True)
    desiel_opening = forms.CharField(required=True)
    desiel_closing = forms.CharField(required=True)
    desiel_price = forms.CharField(required=True)
    product_name = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
    quantity = forms.CharField()
    price = forms.CharField()
    credit_name = forms.CharField()
    amount = forms.CharField()
