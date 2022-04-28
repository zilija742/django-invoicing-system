from django.db import models

class CategoriesModel(models.Model):
    category_code = models.CharField(max_length=30)
    category_description = models.CharField(max_length=200)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.category_code