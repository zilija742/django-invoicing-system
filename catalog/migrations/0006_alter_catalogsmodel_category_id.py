# Generated by Django 3.2.6 on 2022-04-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_catalogsmodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogsmodel',
            name='category_id',
            field=models.CharField(max_length=30),
        ),
    ]
