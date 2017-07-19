from django import forms


class StationForm(forms.Form):
    '''
     Station Form
    '''
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
