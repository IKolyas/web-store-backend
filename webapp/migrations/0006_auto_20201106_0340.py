# Generated by Django 3.1.3 on 2020-11-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20201106_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imagesPath',
        ),
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.ImageField(blank=True, upload_to='products/img/'),
        ),
    ]