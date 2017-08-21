from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from stations.models import Station


class SignUpForm(UserCreationForm):
    stations_list = Station.objects.values_list('id', 'name')

    station = forms.ChoiceField(choices=stations_list, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    location = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('station', 'username', 'first_name', 'last_name',
                  'location', 'password1', 'password2')
