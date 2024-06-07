from django.db import models
from django.utils.translation import gettext_lazy as _


class DiagnosticCategory():

    def __str__(self):
        return f'{self.category_name} | регион: {self.region} '

    class Meta:
        verbose_name = _('Категории диагностики')
        verbose_name_plural = verbose_name


class DiagnosticSubCategory():

    def __str__(self):
        return f'{self.subcategory_name} | регион: {self.region} '

    class Meta:
        verbose_name = _("Подкатегория диагностики")
        verbose_name_plural = verbose_name


class Diagnostic():

    def __str__(self):
        return f' {self.diagnostic_name} | регион: {self.region} '

    class Meta:
        verbose_name = _('услуга: диагностика')
        verbose_name_plural = verbose_name
