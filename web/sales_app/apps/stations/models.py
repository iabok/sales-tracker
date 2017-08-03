from django.urls import reverse
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class Station(models.Model):
    '''
     Station Model
    '''
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def get_absolute_url(self):
        '''
         Url locator for each station
        '''
        return reverse('station-details', kwargs={'pk': self.pk})
