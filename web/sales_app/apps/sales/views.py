from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from sales.forms import SalesForm
from helpers import processSales
from sales.models import Sales, Fuel, ProductSales, Expenses


class SalesFormView(View):
    form_class = SalesForm
    initial = {'key': 'value'}
    template_name = '../templates/sales_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        formData = request.POST
        models = {
          'sales': Sales,
          'fuel': Fuel,
          'productSales': ProductSales,
          'expenses': Expenses
        }
        sales = processSales.Sale(formData, models)
        s = sales.saveData()
        print(s)
        #s.save()
        # print(salesData)
        # print(sales.totalSales())
        # import pdb;
        # pdb.set_trace()
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
