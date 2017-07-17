from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from stations.models import Station
from stations.forms import StationForm


class StationView(FormView):
    '''
      Renders the form
    '''
    template_name = '../templates/station_form.html'
    form_class = StationForm
    success_url = '/success/'


class StationCreate(CreateView):
    '''
     Creates a new station
    '''
    model = Station
    fields = ['name', 'location', 'created_date', 'modified_date']

    # def form_valid(self, form):
    #     '''
    #      Add the current user login
    #     '''
    #     form.instance.created_by = self.request.user
    #     return super(StationCreate, self).form_valid(form)


class StationUpdate(UpdateView):
    '''
     Updates stations
    '''
    model = Station
    fields = ['name', 'location', 'created_date', 'modified_date']


class StationDelete(DeleteView):
    '''
     Deletes a station
    '''
    model = Station
    success_url = reverse_lazy('station-list')
