from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from el_pagination.views import AjaxListView
from accounts.forms import SignUpForm
from accounts.models import Profile


class AccountsFormView(View):
    """
     Form class handler.
    """

    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = '../templates/accounts_create.html'

    def get(self, request, *args, **kwargs):
        """
         Handles get requests
        """
        form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
         Handles post requests
        """
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # load the profile instance created by the signal
            user.refresh_from_db()
            user.profile.station_id = form.cleaned_data.get('station')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect('/home/')

        return render(request, self.template_name, {'form': form})


class accountsList(AjaxListView):
    '''
     List of sales
    '''
    context_object_name = 'accounts'
    template_name = '../templates/accounts_list.html'
    page_template = '../templates/accounts_list_page.html'

    def get_queryset(self):
        '''
         Return all the stations
        '''

        return Profile.objects.all()
