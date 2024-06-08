from django.contrib import admin
from .models import MenuCategory, MenuSubCategory, MenuPosition, PositionOption


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuSubCategory)
class MenuSubCategoryAdmin(admin.ModelAdmin):
    pass


class PositionOptionInline(admin.TabularInline):
    fields = ('option_type_ru', 'option_type_en', 'price')
    model = PositionOption



@admin.register(MenuPosition)
class MenuPositionAdmin(admin.ModelAdmin):
    inlines = [PositionOptionInline]
    fields = ('id', 'title', 'image', 'price', 'note', 'ingredient', 'options')