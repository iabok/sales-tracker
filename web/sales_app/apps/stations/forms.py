from django import forms


class StationForm(forms.Form):
    '''
     Station form
    '''
    name = forms.CharField()
    location = forms.CharField()
