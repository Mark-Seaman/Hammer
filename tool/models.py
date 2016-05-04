from __future__ import unicode_literals
from django.db import models


class Test(models.Model):
    name       = models.CharField (max_length=100)
    output     = models.TextField (null=True, blank=True)
    expected   = models.TextField (null=True, blank=True)
