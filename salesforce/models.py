from django.db import models


# Create your models here.

class SalesForceUsers(models.Model):
    AccountName = models.CharField(max_length=300, blank=True, null=True)
    Type = models.CharField(max_length=300, blank=True, null=True)
    Phone = models.CharField(max_length=20, blank=True, null=True)
