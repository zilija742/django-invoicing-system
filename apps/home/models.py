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

    def type_name(self):
        if self.type == '1':
            return 'RUC'
        elif self.type == '2':
            return 'ID'
        elif self.type == '3':
            return 'VARIOS'
        elif self.type == '4':
            return 'CE'
        elif self.type == '5':
            return 'PST'
        elif self.type == '6':
            return 'PSPT'
        elif self.type == '7':
            return 'ND'
        elif self.type == '8':
            return 'B'
        elif self.type == '9':
            return 'C'
        elif self.type == '10':
            return 'D'
        else: 
            return ''