import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class analysis(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class competitor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class financial(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class market(models.Model):
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name               

