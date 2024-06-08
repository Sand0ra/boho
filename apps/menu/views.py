from rest_framework import generics
from .models import MenuCategory, MenuSubCategory, MenuPosition
from .serializers import MenuCategorySerializer, MenuSubCategorySerializer, MenuPositionSerializer


class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuSubCategoryListView(generics.ListAPIView):
    queryset = MenuSubCategory.objects.all()
    serializer_class = MenuSubCategorySerializer


class MenuPositionDetailView(generics.RetrieveAPIView):
    queryset = MenuPosition.objects.all()
    serializer_class = MenuPositionSerializer
