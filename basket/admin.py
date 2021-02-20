from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from basket.models import Basket


@admin.register(Basket)
class AdminBasket(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'product_id',
        'quantity',
        'create_at',
        'update_at'
    )
    fields = [('user_id', 'product_id', 'quantity',)]
    list_filter = ('product_id', 'user_id')
    # поиск по штрихкоду
    search_fields = ['user_id__startswith']
