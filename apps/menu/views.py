from rest_framework import generics
from .models import DishesCategory, MenuCategory, MenuPosition
from .serializers import DishesCategorySerializer, MenuCategoryListSerializer, MenuCategorySerializer, MenuPositionSerializer


class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategoryListSerializer


class MenuCategoryView(generics.RetrieveAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuPositionDetailView(generics.RetrieveAPIView):
    queryset = MenuPosition.objects.all()
    serializer_class = MenuPositionSerializer


class DishesCategoryListView(generics.ListAPIView):
    queryset = DishesCategory.objects.all()
    serializer_class = DishesCategorySerializer
