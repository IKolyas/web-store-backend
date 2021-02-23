from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='категория', null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


class Subcategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='подкатегория', null=False)
    category = models.ForeignKey(Category,
                                 on_delete=models.RESTRICT,
                                 verbose_name='категория',
                                 related_name='sub',
                                 null=False
                                 )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
        ordering = ('title',)


class Product(models.Model):
    PRODUCT_SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('1', '1 - спальные'),
        ('3', '3 - спальные'),
        ('2', '2 - спальные'),
    ]
    title = models.CharField(max_length=100, verbose_name='наименование', null=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.RESTRICT, verbose_name='подкатегория')
    brief_description = models.TextField(default='', verbose_name='краткое описание')
    description = models.TextField(default='', verbose_name='описание')
    price = models.PositiveIntegerField(null=False, verbose_name='цена')
    size = models.CharField(max_length=20, blank=True, verbose_name='размер')
    color = models.CharField(max_length=16, blank=True, verbose_name='цвет')
    views = models.PositiveBigIntegerField(default=0, verbose_name='просмотры')
    quantity_stock = models.IntegerField(default=0, verbose_name='кол-во на складе')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    barcode = models.IntegerField(blank=True, default='', verbose_name='код товара', unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        ordering = ('title',)


# class Sizes(models.Model):
#     PRODUCT_SIZES = [
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#         ('1', '1 - спальные'),
#         ('1.5', '1.5 - спальные'),
#         ('2', '2 - спальные'),
#     ]
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')
#     size = models.CharField(max_length=50, choices=PRODUCT_SIZES, blank=True)
#
#     class Meta:
#         verbose_name = 'размер'
#         verbose_name_plural = 'Размеры'
#         ordering = ('product_id',)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='img')
    # path = models.ImageField(upload_to='products/img/', blank=True, )

    image_path = models.CharField(max_length=500, default='')
    image_name = models.CharField(max_length=200, default='')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'Картинки'
        ordering = ('product_id',)


class Review(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    for_product = models.ForeignKey(Product, on_delete=models.RESTRICT, null=False)
    if_like = models.BooleanField(null=False, default=1)
    review_text = models.TextField(max_length=1000)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_text

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('from_user_id',)
