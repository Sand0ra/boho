from django.contrib import admin
from .models import DishesCategory, MenuCategory, MenuPosition
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline, TranslationStackedInline



class PositionInline(TranslationStackedInline):
    model = MenuPosition
    fields = ('title', 'price', 'image', 'description')
    extra = 1


@admin.register(MenuPosition)
class MenuPositionAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title',)
    ordering = ('id',)


@admin.register(MenuCategory)
class MenuCategoryAdmin(TabbedTranslationAdmin):
    inlines = (PositionInline, )
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('id',)


@admin.register(DishesCategory)
class DishesCategoryAdmin(TabbedTranslationAdmin):
    inlines = (PositionInline,)
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('id',)
