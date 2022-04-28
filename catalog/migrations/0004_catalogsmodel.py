# Generated by Django 3.2.6 on 2022-04-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_categoriesmodel_category_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('type', models.IntegerField()),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('sunat_code', models.CharField(max_length=20)),
                ('currency', models.IntegerField(null=True)),
                ('affectation_type', models.IntegerField(null=True)),
                ('sale_without_igv', models.IntegerField(null=True)),
                ('sale_with_igv', models.IntegerField(null=True)),
                ('purchase_without_igv', models.IntegerField(null=True)),
                ('purchase_with_igv', models.IntegerField(null=True)),
            ],
        ),
    ]