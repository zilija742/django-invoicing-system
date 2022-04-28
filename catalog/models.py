from unicodedata import category
from django.db import models

class CategoriesModel(models.Model):
    category_code = models.CharField(max_length=30)
    category_description = models.CharField(max_length=200)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.category_code

class CatalogsModel(models.Model):
    category_id = models.CharField(max_length=30)
    type = models.IntegerField(null=False)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    sunat_code = models.CharField(max_length=20)
    currency = models.IntegerField(null=True)
    affectation_type = models.IntegerField(null=True)
    sale_without_igv = models.IntegerField(null=True)
    sale_with_igv = models.IntegerField(null=True)
    purchase_without_igv = models.IntegerField(null=True)
    purchase_with_igv = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name