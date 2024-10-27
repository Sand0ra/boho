from modeltranslation.translator import TranslationOptions, register
from .models import DishesCategory, MenuCategory, MenuPosition


@register(MenuCategory)
class MenuCategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(DishesCategory)
class MenuCategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(MenuPosition)
class MenuPositionTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )

