# Generated by Django 3.2.6 on 2022-04-29 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_catalogsmodel_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogsmodel',
            old_name='category_id',
            new_name='category',
        ),
    ]