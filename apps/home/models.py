# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EntitiesModel(models.Model):
    number = models.CharField(max_length=11)
    type = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    primary_email = models.CharField(max_length=200)
    first_email = models.CharField(max_length=200, null=True)
    second_email = models.CharField(max_length=200, null=True)
    mobile_number = models.CharField(max_length=200, null=True)
    fijo = models.CharField(max_length=200, null=True)
    client_detraccion = models.CharField(max_length=200, null=True)
    detail = models.CharField(max_length=200, null=True)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.number