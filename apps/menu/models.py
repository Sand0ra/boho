from django.db import models
from django.utils.translation import gettext_lazy as _


class MenuCategory(models.Model):
    title = models.CharField(
        max_length=90,
        null=True,
        blank=True,
        verbose_name=_("Название")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория меню")
        verbose_name_plural = _("Категории меню")



class DishesCategory(models.Model):
    title = models.CharField(
        max_length=90,
        verbose_name=_("Название")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория блюда")
        verbose_name_plural = _("Категории блюд")



class MenuPosition(models.Model):
    category = models.ForeignKey(
        to=MenuCategory,
        on_delete=models.DO_NOTHING,
        null=True, blank=True,
        related_name='positions',
        verbose_name=_("Категории")
    )
    dishes = models.ForeignKey(
        to=DishesCategory,
        on_delete=models.DO_NOTHING,
        null=True, blank=True,
        related_name='positions',
        verbose_name=_("Блюда")
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
    description = models.TextField(
        _("Описание"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Позиция меню")
        verbose_name_plural = _("Позиции меню")
