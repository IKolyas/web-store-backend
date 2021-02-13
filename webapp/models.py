from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


class Subcategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', related_name='sub')

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
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='подкатегория')
    title = models.CharField(max_length=100, null=False, verbose_name='наименование')
    description = models.TextField(default='', verbose_name='описание')
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2, verbose_name='цена')
    size = models.CharField(max_length=5, choices=PRODUCT_SIZES, blank=True, verbose_name='размер')
    color = models.CharField(max_length=16, blank=True, verbose_name='цвет')
    quantity_views = models.IntegerField(default=0, verbose_name='просмотров')
    quantity_orders = models.IntegerField(default=0, verbose_name='заказов')
    quantity_stock = models.IntegerField(default=0, verbose_name='на складе')
    is_active = models.BooleanField(default=True, verbose_name='наличие товара')

    # добавить уникальность
    barcode = models.IntegerField(blank=True, default='', verbose_name='штрихкод')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        ordering = ('created',)


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
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='img')
    path = models.ImageField(upload_to='products/img/', blank=True, )

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'Картинки'
        ordering = ('product_id',)


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    review = models.TextField(default='')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('created',)
