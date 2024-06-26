from rest_framework import generics
from .models import MenuCategory, MenuSubCategory, MenuPosition, Event, Chart
from .serializers import MenuCategorySerializer, MenuSubCategorySerializer, MenuPositionSerializer, EventSerializer, \
    ChartSerializer


class MenuCategoryListView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuSubCategoryListView(generics.ListAPIView):
    queryset = MenuSubCategory.objects.all()
    serializer_class = MenuSubCategorySerializer


class MenuPositionDetailView(generics.RetrieveAPIView):
    queryset = MenuPosition.objects.all()
    serializer_class = MenuPositionSerializer


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ChartListView(generics.ListAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
