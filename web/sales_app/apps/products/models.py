from django.urls import reverse
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class Product(models.Model):
    '''
     Product Model
    '''
    name = models.CharField(max_length=200)
    unit_price = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def get_absolute_url(self):
        '''
         Redirect to the product details page
        '''
        return reverse('product-details', kwargs={'pk': self.pk})
