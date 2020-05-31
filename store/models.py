import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.store_name