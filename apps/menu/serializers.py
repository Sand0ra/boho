from rest_framework import serializers
from .models import DishesCategory, MenuCategory, MenuPosition


class MenuPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuPosition
        fields = ['id', 'title', 'image', 'price', 'description',]



class MenuCategorySerializer(serializers.ModelSerializer):
    positions = MenuPositionSerializer(many=True)

    class Meta:
        model = MenuCategory
        fields = ('id', 'title', 'image', 'positions')


class MenuCategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCategory
        fields = ('id', 'title','image')


class DishesCategorySerializer(serializers.ModelSerializer):
    positions = MenuPositionSerializer(many=True)

    class Meta:
        model = DishesCategory
        fields = ('id', 'title', 'positions')
