from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Task
class Task (models.Model):
    name     = models.CharField (max_length=100)
    notes    = models.TextField (null=True, blank=True)
    date     = models.DateField (default=now)
    hours    = models.IntegerField (default=0)
    done     = models.BooleanField (default=False)
    # project  = models.ForeignKey (Project) 
    # worker   = models.ForeignKey (User) 
