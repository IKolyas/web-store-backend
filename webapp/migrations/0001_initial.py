# Generated by Django 3.1.3 on 2020-11-05 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='наименование')),
                ('description', models.TextField(default='', verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, verbose_name='размер')),
                ('quantity_views', models.IntegerField(default=0, verbose_name='просмотров')),
                ('quantity_orders', models.IntegerField(default=0, verbose_name='заказов')),
                ('quantity_stock', models.IntegerField(default=0, verbose_name='на складе')),
                ('barcode', models.IntegerField(blank=True, default='', verbose_name='УИН')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.category')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=50)),
                ('review', models.TextField(default='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.subcategory', verbose_name='подкатегория'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='products/img/')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='webapp.product')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'Картинки',
                'ordering': ('product_id',),
            },
        ),
    ]