from django.db import models

class PurchasesModel(models.Model):
    entity = models.ForeignKey('home.EntitiesModel', on_delete=models.CASCADE)
    document_type = models.IntegerField(null=False)
    broadcast_date = models.DateField(auto_now=True)
    currency = models.IntegerField(null=False)
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=10)
    series = models.CharField(max_length=10)
    number = models.IntegerField(null=False)
    catalog = models.ForeignKey('catalog.CatalogsModel', on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.series + self.number