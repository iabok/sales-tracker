'''
 Products views
'''
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from el_pagination.views import AjaxListView
from products.models import Product


class ProductCreate(CreateView):
    '''
     Creates a new product
    '''
    model = Product
    template_name = '../templates/product_create.html'
    fields = ['name', 'unit_price']


class ProductUpdate(UpdateView):
    '''
     Updates product
    '''
    model = Product
    template_name = '../templates/product_update.html'
    fields = ['name', 'unit_price']


class ProductDelete(DeleteView):
    '''
     Deletes a product
    '''
    model = Product
    template_name = '../templates/product_confirm_delete.html'
    success_url = reverse_lazy('product-add')


class ProductList(AjaxListView):
    '''
     List of product
    '''
    context_object_name = "products"
    template_name = '../templates/product_list.html'
    page_template = '../templates/product_list_page.html'

    def get_queryset(self):
        '''
         Return all the stations
        '''
        return Product.objects.all()


class ProductDetail(DetailView):
    '''
     View station details
    '''
    model = Product
    template_name = '../templates/product_detail.html'
