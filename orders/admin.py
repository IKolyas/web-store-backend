from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from orders.models import Orders, OrderProduct
from django.contrib.auth.models import User


@admin.register(Orders)
class AdminOrders(admin.ModelAdmin):
    list_display = (
        'user_id',
        'order_status',
        'create_at',
        'update_at'
    )
    list_filter = ('user_id', 'order_status')
    # поиск по штрихкоду
    search_fields = ['user_id__startswith']


@admin.register(OrderProduct)
class AdminOrders(admin.ModelAdmin):
    list_display = (
        'order_id',
        'product_id',
        'quantity',
        'create_at',
        'update_at'
    )
    list_filter = ('order_id', 'product_id', 'quantity')
    # поиск по штрихкоду
    search_fields = ['order_id__startswith', 'product_id__startswith']
