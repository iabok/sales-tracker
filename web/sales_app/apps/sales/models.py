"""
 Model definitions for sales
"""
from django.urls import reverse
from django.db import models
from django.utils import timezone
from stations.models import Station
from simple_history.models import HistoricalRecords


class Sales(models.Model):
    '''
     Sales Model
    '''
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    sales_date = models.DateField()
    total_sales = models.IntegerField()
    total_expenses = models.IntegerField()
    total_revenue = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def get_absolute_url(self):
        '''
         Redirect to the product details page
        '''
        return reverse('sales-list')


class Fuel(models.Model):
    '''
     Fuel Model
    '''
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    opening_meter = models.IntegerField()
    closing_meter = models.IntegerField()
    unit_price = models.IntegerField()
    sales_date = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()


class ProductSales(models.Model):
    '''
     Product Sales Model
    '''
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    product_name = models.IntegerField()
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    sales_date = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()


class Expenses(models.Model):
    '''
     Expenses Model
    '''
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.IntegerField()
    amount = models.IntegerField()
    sales_date = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()
