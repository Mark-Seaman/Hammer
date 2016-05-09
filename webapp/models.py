from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Web App
class WebApp (models.Model):
    name     = models.CharField (max_length=100)
    notes    = models.TextField (null=True, blank=True)
    # project  = models.ForeignKey (Project) 
    # worker   = models.ForeignKey (User) 
