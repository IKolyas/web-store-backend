from django.urls import path, re_path

from .views import ArticleOneView, DrawCategoriesView, ProductsFilterCategoryView, ProductSizesView, BasketView

app_name = 'webapp'

urlpatterns = [
    path('products/', ProductsFilterCategoryView.as_view(), name='product_filter'),
    path('products/dropdown_categories/', DrawCategoriesView.as_view(), name='draw_categories'),
    path('products/category_sizes/', ProductSizesView.as_view(), name='product_sizes'),
    path(r'products/article/', ArticleOneView.as_view(), name='product_one'),
    path('basket/', BasketView.as_view(), name='basket'),
]
