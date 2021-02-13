from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework import filters

from .serializers import ProductSerializer, CategorySerializer, ProductSizesSerializer, BasketProductsSerializer
from .models import Product, Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Pagination
class DefaultPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 2000


# Фильтр по каталогу продуктов
class ProductFilter(rest_framework.FilterSet):
    price_min = rest_framework.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = rest_framework.NumberFilter(field_name="price", lookup_expr='lte')
    sizes = rest_framework.CharFilter(field_name='size', lookup_expr='in')
    product = rest_framework.CharFilter(field_name='product')

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'product', 'sizes', 'price_min', 'price_max']


# Фильтр по id карзины
class BasketFilter(rest_framework.FilterSet):
    ids = rest_framework.NumberFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['id']


#
# class ProductsSetPagination(PageNumberPagination):
#     page_size = 4
#     page_size_query_param = 'page_size'
#     max_page_size = 200


# МЕНЮ КАТЕГОРИЙ
class DrawCategoriesView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


# СПИСОК ПРОДУКТОВ
class ProductsView(generics.ListAPIView):
    # список
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    # pagination_class = ProductsSetPagination

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    # def list(self, request, *args, **kwargs):
    #     queryset = Product.objects.all()
    #     serializer = ProductSerializer(queryset, many=True)
    #
    #     return Response(serializer.data)


#  ФИЛЬТР ПРОДУКТОВ
# class ProductsFilterCategoryView(generics.ListAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = ProductSerializer
#
#     # pagination_class = ProductsSetPagination
#
#     def get_queryset(self):
#         queryset = Product.objects.all().exclude(quantity_stock=0)
#         category = self.request.query_params.get('category', None)
#         subcategory = self.request.query_params.get('subcategory', None)
#         sizes = self.request.query_params.get('sizes', None)
#         product = self.request.query_params.get('product', None)
#         price_min = self.request.query_params.get('price_min', None)
#         price_max = self.request.query_params.get('price_max', None)
#         sort = self.request.query_params.get('sort', None)
#         search = self.request.query_params.get('search', None)
#
#         if category is not None:
#             queryset = queryset.filter(category_id=category)
#         if subcategory is not None:
#             queryset = queryset.filter(subcategory_id=subcategory)
#         if sizes is not None:
#             queryset = queryset.filter(size__in=sizes)
#         if product is not None:
#             queryset = queryset.filter(id=product)
#         if price_min is not None and price_max is not None:
#             queryset = queryset.filter(price__gte=price_min, price__lte=price_max)
#         if search is not None:
#             queryset = queryset.filter(title__in=search)
#         if sort is not None:
#             queryset = queryset.order_by(sort) if sort == 'title' else queryset.order_by(sort).reverse()
#
#         return queryset

class ProductsFilterCategoryView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all().exclude(quantity_stock=0)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['title', 'price', 'quantity_views']


class ProductSizesView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSizesSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = Product.objects.values('size').distinct()

        category = self.request.query_params.get('category', None)
        subcategory = self.request.query_params.get('subcategory', None)

        if category is not None:
            queryset = queryset.filter(category_id=category)
        if subcategory is not None:
            queryset = queryset.filter(subcategory_id=subcategory)

        return queryset


class ArticleOneView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = self.request.query_params.get('id', None)
        queryset = Product.objects.filter(pk=product)
        return queryset


class BasketView(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = BasketProductsSerializer

    def get_queryset(self):
        id_string = self.request.query_params.get('id', None)
        if id_string is not None:
            ids = [int(id) for id in id_string.split(',')]

            queryset = Product.objects.filter(pk__in=list(ids))
            print(queryset)
            return queryset

