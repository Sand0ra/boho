from django.urls import path
from .views import MenuCategoryListView, MenuCategoryView, MenuPositionDetailView, DishesCategoryListView

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
    path('category/<int:pk>/', MenuCategoryView.as_view(), name='menu-category-detail'),
    path('position/<int:pk>/', MenuPositionDetailView.as_view(), name='menu-position-detail'),
    path('dishes/', DishesCategoryListView.as_view(), name='dishes-category-list'),
]
