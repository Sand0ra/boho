from django.db import models
from django.utils.translation import gettext_lazy as _

class MenuCategory(models.Model):
    title = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=_("Название")
    )

    # def __str__(self):
        # return self.title

    class Meta:
        verbose_name = _("Категория меню")
        verbose_name_plural = _("Категории меню")


class MenuSubCategory(models.Model):
    category = models.ForeignKey(
        to=MenuCategory,
        on_delete=models.DO_NOTHING,
        related_name='category_rel',
        verbose_name=_("Категория")
    )
    title = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=_("Название")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Подкатегория меню")
        verbose_name_plural = _("Подкатегории меню")


class MenuPosition(models.Model):
    subcategory = models.ForeignKey(
        to=MenuSubCategory,
        on_delete=models.DO_NOTHING,
        related_name='subcategory_rel',
        verbose_name=_("Подкатегория")
    )
    title = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=_("Название")
    )
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("Изображение"),
        upload_to=_("menu_img/")
    )
    price = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Цена")
    )
    note = models.TextField(
        _("Примечание"),
        null=True,
        blank=True
    )
    ingredient = models.TextField(
        _("Ингредиенты"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Позиция меню")
        verbose_name_plural = _("Позиции меню")


class PositionOption(models.Model):
    menu_position = models.ForeignKey(
        MenuPosition,
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name=_("Позиция меню")
    )
    option_type = models.CharField(
        max_length=50,
        verbose_name=_("Тип опции")
    )
    price = models.IntegerField(
        verbose_name=_("Цена")
    )

    def __str__(self):
        return f"{self.menu_position.title} - {self.option_type}"

    class Meta:
        verbose_name = _("Опция позиции")
        verbose_name_plural = _("Опции позиции")
