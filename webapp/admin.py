from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from webapp.models import Category, Subcategory, Product,  Image, Review


class Gallery(admin.TabularInline):
    fk_name = 'product_id'
    model = Image

#
# class Size(admin.TabularInline):
#     fk_name = 'product_id'
#     model = Sizes


class Catalog(admin.TabularInline):
    fk_name = 'subcategory'
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory')

    def subcategory(self, obj):
        count = Subcategory.objects.filter(category=obj.id).count()
        url = (
                reverse("admin:webapp_subcategory_changelist")
                + "?"
                + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} подкатегорий</a>')

    subcategory.short_description = "подкатегорий"


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    inlines = [Catalog]
    list_display = ('title', 'category', 'products')

    # def products(self, obj):
    #     result = len(Product.objects.filter(subcategory_id=obj))
    #     return result

    def products(self, obj):
        count = Product.objects.filter(subcategory_id=obj).count()
        url = (
                reverse("admin:webapp_product_changelist")
                + "?"
                + urlencode({"subcategory__id": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} продуктов</a>')

    products.short_description = "кол-во"


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [Gallery]
    list_display = (
    'title', 'category', 'subcategory', 'price', 'size', 'color', 'quantity_stock', 'quantity_views', 'barcode', 'created', 'is_active')
    fields = ['title', ('category', 'subcategory'), ('price', 'size', 'color',), ('quantity_stock', 'quantity_views', 'is_active', 'barcode')]
    list_filter = ('category', 'subcategory', 'created')
    # поиск по штрихкоду
    search_fields = ['barcode__startswith']

    # Подсветка остатков
    # def mark_few_stock(self, obj):
    #     quantity = obj.quantity_stock
    #     result = quantity
    #     if quantity == 0:
    #         result = format_html(f'<b>{result}!!!</b>')
    #     elif quantity < 4:
    #         result = format_html(f'<b>{result}!!</b>')
    #     elif quantity < 8:
    #         result = format_html(f'<b>{result}!</b>')
    #
    #     return result
    #
    # mark_few_stock.short_description = 'на складе'

    # деление на секции
    # fieldsets = (
    #     (None, {
    #         'fields': ('book','imprint', 'id')
    #     }),
    #     ('Availability', {
    #         'fields': ('status', 'due_back')
    #     }),
    # )


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    # product = Product.objects.get()
    list_display = ('id', 'product_id', 'path', 'get_image')
    list_filter = ('product_id',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="/media/{obj.path}" width="50" height="50">')

    get_image.short_description = 'Картинки'


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    pass
