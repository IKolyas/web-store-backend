# Generated by Django 3.1.3 on 2021-02-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20210214_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(verbose_name='цена'),
        ),
    ]
