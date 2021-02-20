from django.db import models
from django.contrib.auth.models import User
from webapp.models import Product
from django.utils import timezone

# Create your models here.
class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT, null=False)
    quantity = models.PositiveIntegerField(null=False, default=1)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'Корзины пользователей'
        ordering = ('create_at',)
