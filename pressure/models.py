from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class BloodPressure(models.Model):
    author = models.ForeignKey('auth.User')
    systolic_value = models.IntegerField()
    diastolic_value = models.IntegerField()
    pulse =  models.IntegerField()
    comment = models.TextField()
    add_date_time = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.add_date_time)
