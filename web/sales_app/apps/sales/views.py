from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from el_pagination.views import AjaxListView
from helpers import processSales
from sales.models import Sales, Fuel, ProductSales, Expenses
from sales.forms import SalesForm


class SalesFormView(View):
    form_class = SalesForm
    initial = {'key': 'value'}
    template_name = '../templates/sales_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            formData = request.POST
            models = {
              'sales': Sales,
              'fuel': Fuel,
              'productSales': ProductSales,
              'expenses': Expenses
            }

            processSales.Sale(formData, models).saveData()
            return reverse_lazy('sales-list')

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
    model = Sales
    template_name = '../templates/sales_detail.html'
