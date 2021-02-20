from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profiles(models.Model):
    GENDER = [
        ('m', 'м'),
        ('f', 'ж')
    ]
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField(db_index=True)
    hometown = models.CharField(max_length=200)
    balance = models.PositiveBigIntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'
        ordering = ('create_at',)
