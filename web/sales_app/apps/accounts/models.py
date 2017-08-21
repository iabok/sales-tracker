from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from stations.models import Station
from simple_history.models import HistoricalRecords


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
