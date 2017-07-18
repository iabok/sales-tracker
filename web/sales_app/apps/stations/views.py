'''
 Stations views
'''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from stations.models import Station
# from stations.forms import StationForm


# class StationView(FormView):
#     '''
#      Creates and saves our form
#     '''
#     template_name = '../templates/station_add_form.html'
#     form_class = StationForm
#     success_url = '/thanks/'
#
#     def form_valid(self, form):
#         '''
#          Saves our form
#         '''
#         return super(StationView, self).form_valid(form)

class StationCreate(CreateView):
    '''
     Creates a new station
    '''
    model = Station
    template_name = '../templates/station_add_form.html'
    fields = ['name', 'location']

    # def form_valid(self, form):
    #     '''
    #      Save our form
    #     '''
    #     # form.instance.created_by = self.request.user
    #     return super(StationCreate, self).form_valid(form)


class StationUpdate(UpdateView):
    '''
     Updates stations
    '''
    model = Station
    template_name = '../templates/station_edit_form.html'
    fields = ['name', 'location']


class StationDelete(DeleteView):
    '''
     Deletes a station
    '''
    model = Station
    success_url = reverse_lazy('station-list')
