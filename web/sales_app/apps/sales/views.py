from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from sales.forms import SalesForm
from helpers import processSales

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
        salesData = {
            'petrol_open': formData['petrol_open'],
            'petrol_close': formData['petrol_close'],
            'petrol_price': formData['petrol_price'],
            'desiel_open': formData['desiel_open'],
            'desiel_close': formData['desiel_close'],
            'desiel_price': formData['desiel_price'],
            'product_name': formData.getlist('product_name'),
            'quantity': formData.getlist('quantity'),
            'price': formData.getlist('price'),
            'credit_name': formData.getlist('credit_name'),
            'amount': formData.getlist('amount')
        }
        sales = processSales.Sales(salesData)
        # print(salesData)
        # print(sales.totalSales())
        # import pdb;
        # pdb.set_trace()
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
