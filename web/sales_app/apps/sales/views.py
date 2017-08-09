from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from sales.forms import SalesForm

class SalesFormView(View):
    form_class = SalesForm
    initial = {'key': 'value'}
    template_name = '../templates/sales_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        import pdb;
        pdb.set_trace()
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
