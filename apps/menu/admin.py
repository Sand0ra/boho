from django.contrib import admin
from .models import MenuCategory, MenuSubCategory, MenuPosition, PositionOption, Event
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline


@admin.register(MenuCategory)
class MenuCategoryAdmin(TabbedTranslationAdmin):

    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('id', )


@admin.register(MenuSubCategory)
class MenuSubCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title',)
    ordering = ('id', )


class PositionOptionInline(TranslationTabularInline):
    model = PositionOption

    def get_max_num(self, request, obj=None, **kwargs):
        return 2


@admin.register(MenuPosition)
class MenuPositionAdmin(TabbedTranslationAdmin):
    inlines = [PositionOptionInline]
    list_display = ('id', 'title', 'subcategory')
    list_display_links = ('id', 'title',)
    ordering = ('id', )


@admin.register(Event)
class EventsAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('id', )
