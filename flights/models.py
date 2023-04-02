from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    
