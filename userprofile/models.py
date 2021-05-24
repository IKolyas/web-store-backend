from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER = [
        ('m', 'м'),
        ('f', 'ж')
    ]
    user = models.OneToOneField(User, on_delete=models.RESTRICT, null=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField(db_index=True)
    hometown = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    balance = models.PositiveBigIntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'
        ordering = ('create_at',)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
