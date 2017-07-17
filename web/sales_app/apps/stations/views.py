from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from stations.models import Station


class StationCreate(CreateView):
    '''
     Creates a new station
    '''
    model = Station
    template_name = '../templates/station_form.html'
    fields = ['name', 'location']

    def form_valid(self, form):
        '''
         Save our form
        '''
        # form.instance.created_by = self.request.user
        return super(StationCreate, self).form_valid(form)


class StationUpdate(UpdateView):
    '''
     Updates stations
    '''
    model = Station
    fields = ['name', 'location']


class StationDelete(DeleteView):
    '''
     Deletes a station
    '''
    model = Station
    success_url = reverse_lazy('station-list')
