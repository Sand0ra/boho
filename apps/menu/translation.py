from modeltranslation.translator import TranslationOptions, register
from .models import MenuCategory, MenuSubCategory, MenuPosition, PositionOption, Event


@register(MenuCategory)
class MenuCategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(MenuSubCategory)
class MenuSubcategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(MenuPosition)
class MenuPositionTranslationOptions(TranslationOptions):
    fields = ('ingredient', 'title', 'note', )


@register(PositionOption)
class PositionOptionTranslationOptions(TranslationOptions):
    fields = ('option_type', )


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
