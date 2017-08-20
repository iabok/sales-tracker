from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from el_pagination.views import AjaxListView
from helpers import processSales
from sales.models import Sales, Fuel, ProductSales, Expenses
from stations.models import Station
from sales.forms import SalesForm


class SalesFormView(View):
    """
     Form class handler.
    """

    form_class = SalesForm
    initial = {'key': 'value'}
    template_name = '../templates/sales_create.html'

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
        form = self.form_class(request.POST)
        if form.is_valid():
            formData = request.POST
            models = {
              'sales': Sales,
              'fuel': Fuel,
              'productSales': ProductSales,
              'expenses': Expenses
            }

            # saves the sales form
            processSales.Sale(formData, models).saveData()

            return HttpResponseRedirect('/sales/')

        return render(request, self.template_name, {'form': form})


class SalesList(AjaxListView):
    '''
     List of sales
    '''
    context_object_name = 'sales'
    template_name = '../templates/sales_list.html'
    page_template = '../templates/sales_list_page.html'

    def get_queryset(self):
        '''
         Return all the stations
        '''

        return Sales.objects.all()


class SalesDetail(DetailView):
    '''
     View sales details
    '''

    context_object_name = 'sales'
    model = Sales
    template_name = '../templates/sales_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SalesDetail, self).get_context_data(**self.kwargs)
        context['Fuel'] = Fuel.objects.filter(sales_id=self.kwargs['pk'])
        context['Products'] = ProductSales.objects.filter(
                              sales_id=self.kwargs['pk'])
        context['Expenses'] = Expenses.objects.filter(
                              sales_id=self.kwargs['pk'])
        return context
