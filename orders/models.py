from django.contrib.auth.models import User
from webapp.models import Product
from django.db import models


# Create your models here.
class Orders(models.Model):
    ORDER_STATUS = [
        ('pending payment', 'ppay'),
        ('paid', 'paid'),
        ('delivered', 'deliv'),
        ('issued', 'issued'),
    ]
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    order_status = models.CharField(max_length=32, choices=ORDER_STATUS)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = 'заказы'
        verbose_name_plural = 'Заказы'
        ordering = ('create_at',)


class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.PositiveIntegerField(null=False, default=1)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order_id}'

    class Meta:
        verbose_name = 'продукты в заказах'
        verbose_name_plural = 'Продукты в заказах'
        ordering = ('create_at',)
