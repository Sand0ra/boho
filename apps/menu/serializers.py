from rest_framework import serializers
from .models import MenuCategory, MenuSubCategory, MenuPosition, PositionOption


class PositionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionOption
        fields = ['id', 'option_type', 'price']


class MenuPositionSerializer(serializers.ModelSerializer):
    options = PositionOptionSerializer(read_only=True, many=True)

    class Meta:
        model = MenuPosition
        # fields = ['id', 'title', 'image', 'price', 'note', 'ingredient', 'options']
        fields = '__all__'


class MenuSubCategorySerializer(serializers.ModelSerializer):
    subcategory_rel = MenuPositionSerializer(read_only=True, many=True)

    class Meta:
        model = MenuSubCategory
        fields = ('id', 'title', 'subcategory_rel')


class MenuSubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ('id', 'title',)


class MenuCategorySerializer(serializers.ModelSerializer):
    category_rel = MenuSubCategoryListSerializer(read_only=True, many=True)

    class Meta:
        model = MenuCategory
        fields = ('id', 'title', 'category_rel')
