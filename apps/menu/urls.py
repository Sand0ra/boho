from django.urls import path
from .views import MenuCategoryListView, MenuSubCategoryListView, MenuPositionDetailView

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='category-list'),
    path('subcategories/', MenuSubCategoryListView.as_view(), name='subcategory-list'),
    path('positions/<int:pk>/', MenuPositionDetailView.as_view(), name='position-detail'),
]
