"""
 Model definitions for funds
"""
from django.urls import reverse
from django.db import models
from django.utils import timezone
from stations.models import Station
from simple_history.models import HistoricalRecords


class Bank(models.Model):
    '''
     Bank Model
    '''
    amount = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def get_absolute_url(self):
        '''
         Redirect to the product details page
        '''
        return reverse('bank-list')


class Wallet(models.Model):
    '''
     Wallet Model
    '''
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def get_absolute_url(self):
        '''
         Redirect to the Wallet details page
        '''
        return reverse('wallet-details', kwargs={'pk': self.pk})
