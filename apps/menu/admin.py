from django.contrib import admin
from .models import MenuCategory, MenuSubCategory, MenuPosition, PositionOption, Event


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {
            'fields': ['title',]
        }),
        ('Английский перевод', {
            'fields': ['title_en', ]
        }),
    ]

    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('id', )


@admin.register(MenuSubCategory)
class MenuSubCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {
            'fields': ['category', 'title',]
        }),
        ('Английский перевод', {
            'fields': ['title_en', ]
        }),
    ]

    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title',)
    ordering = ('id', )


class PositionOptionInline(admin.TabularInline):
    fields = ('option_type_ru', 'option_type_en', 'price')
    model = PositionOption


@admin.register(MenuPosition)
class MenuPositionAdmin(admin.ModelAdmin):
    inlines = [PositionOptionInline]
    fieldsets = [
        ('Русский перевод', {
            'fields': ['subcategory', 'title', 'image', 'price', 'note', 'ingredient']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'note_en', 'ingredient_en']
        }),
    ]

    list_display = ('id', 'title', 'subcategory')
    list_display_links = ('id', 'title',)
    ordering = ('id', )


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Русский перевод', {
            'fields': ['title', 'image', 'description']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en']
        }),
    ]

    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    ordering = ('id', )
