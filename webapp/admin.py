from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from webapp.models import Category, Subcategory, Product, Image, Review
from django.contrib.auth.models import User


class Gallery(admin.TabularInline):
    fk_name = 'product'
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
    list_display = ('title', 'subcategory', 'create_at', 'update_at')

    def subcategory(self, obj):
        count = Subcategory.objects.filter(category_id=obj.id).count()
        url = (
                reverse("admin:webapp_subcategory_changelist")
                + "?"
                + urlencode({"category": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} подкатегорий</a>')

    subcategory.short_description = "подкатегорий"


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    inlines = [Catalog]
    list_display = ('title', 'category_id', 'products', 'create_at', 'update_at')
    list_filter = ('category_id', 'create_at')

    def products(self, obj):
        count = Product.objects.filter(subcategory_id=obj).count()
        url = (
                reverse("admin:webapp_product_changelist")
                + "?"
                + urlencode({"subcategory": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">{count} продуктов</a>')

    products.short_description = "кол-во"


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [Gallery]
    list_display = (
        'title',
        'subcategory',
        'price',
        'size',
        'color',
        'quantity_stock',
        'views',
        'rating',
        'barcode',
        'image',
        'reviews',
        'create_at',
        'update_at')
    fields = [('title', 'subcategory',), ('price', 'size', 'color',),
              ('brief_description', 'description',),
              ('quantity_stock', 'views', 'rating', 'barcode')]
    list_filter = ('subcategory_id__category_id', 'subcategory_id', 'create_at')
    # поиск по штрихкоду
    search_fields = ['barcode__startswith']

    def image(self, obj):
        count = Image.objects.filter(product_id=obj.id).count()
        url = (
                reverse("admin:webapp_image_changelist")
                + "?"
                + urlencode({"image": f"{obj.id}"})
        )

        return format_html(f'<a href="{url}">{count} шт</a>')

    image.short_description = "картинки"

    def reviews(self, obj):
        count = Review.objects.filter(for_product_id=obj.id).count()
        url = (
                reverse("admin:webapp_review_changelist")
                + "?"
                + urlencode({"review": f"{obj.id}"})
        )

        return format_html(f'<a href="{url}">{count} шт</a>')

    reviews.short_description = "отзывы"

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
    list_display = ('id', 'product_id', 'image_path', 'image_name', 'get_image')
    list_filter = ('product_id',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image_path}{obj.image_name}" width="50" height="50">')

    get_image.short_description = 'Картинки'


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'if_like', 'review_text', 'create_at', 'update_at')
    fields = [('from_user_id', 'for_product_id', 'if_like'),
              'review_text']

    list_filter = ('from_user_id', 'for_product_id')

    def product(self, obj):
        product = Product.objects.get(id=obj.id)
        url = (
                reverse("admin:webapp_product_changelist")
                + "?"
                + urlencode({"product": f"{obj.id}"})
        )

        return format_html(f'<a href="{url}"> {product} </a>')

    product.short_description = "продукт"

    def user(self, obj):
        user = User.objects.get(id=obj.id)
        url = (
                reverse("admin:auth_user_changelist")
                + "?"
                + urlencode({"user": f"{obj.id}"})
        )

        return format_html(f'<a href="{url}"> {user} </a>')

    user.short_description = "пользователь"
