from django.utils.safestring import mark_safe
from rest_framework import serializers
from webapp.models import Category, Subcategory, Product, Image, Review


class SubcategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # category_title = serializers.IntegerField(source='subcategory_id.category_id.title', read_only=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'category_id',)


class CategorySerializer(serializers.ModelSerializer):
    sub = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'sub')

    # def create(self, validated_data):
    #     subject = Subcategory.objects.create(parent=validated_data['category']['title'],
    #                                          child_name=validated_data['sub'])
    #
    #     return subject


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_path', 'image_name')

    def create(self, validated_data):
        subject = Image.objects.create(parent=validated_data['product']['id'], child_name=validated_data['img'])

        return subject


# class SizesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sizes
#         fields = ('id', 'size')
#
#     def create(self, validated_data):
#         subject = Sizes.objects.create(parent=validated_data['product']['id'], child_name=validated_data['size'])
#         return subject


class ProductSerializer(serializers.ModelSerializer):
    # category_id = serializers.CharField(source='category.title', read_only=True)
    # subcategory_id = serializers.CharField(source='subcategory.title', read_only=True)
    # subcategory = SubcategorySerializer()
    subcategory_id = serializers.IntegerField(source='subcategory_id.id', read_only=True)
    category_id = serializers.IntegerField(source='subcategory_id.category_id.id', read_only=True)
    # category_id = subcategory_id.Meta
    # category_id = CategorySerializer()
    img = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'subcategory_id',
            'category_id',
            'title',
            'brief_description',
            'description',
            'price',
            'size',
            'color',
            'views',
            'quantity_stock',
            'create_at',
            'update_at',
            'barcode',
            'img'
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSizesSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source='category.id', read_only=True)
    subcategory_id = serializers.CharField(source='subcategory.id', read_only=True)

    class Meta:
        model = Product
        fields = 'category_id', 'subcategory_id', 'size'


# Сериализация корзины
class BasketProductsSerializer(serializers.ModelSerializer):
    img = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'img', 'price', 'size', 'color']
