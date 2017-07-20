'''
 Stations views
'''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from el_pagination.views import AjaxListView
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
    template_name = '../templates/station_create.html'
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
    template_name = '../templates/station_update.html'
    fields = ['name', 'location']


class StationDelete(DeleteView):
    '''
     Deletes a station
    '''
    model = Station
    template_name = '../templates/station_confirm_delete.html'
    success_url = reverse_lazy('station-add')


class StationList(AjaxListView):
    '''
     List of stations
    '''
    context_object_name = "stations"
    template_name = '../templates/station_list.html'
    page_template = '../templates/station_list_page.html'


    def get_queryset(self):
        '''
         Return all the stations
        '''
        return Station.objects.all()


class StationDetail(DetailView):
    '''
     View station details
    '''
    model = Station
    template_name = '../templates/station_detail.html'
