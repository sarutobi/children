# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserType(models.Model):
    class Meta:
        order = ('order')

    name = models.CharField(imax_length=20, verbose_name=_('Наименование'))
    description = models.Text(
        verbose_name=_('Описание'),
        blank=True,
        null=True)
#    icon = models.ImageField()
    order = models.IntegerField(verbose_name=_('Порядок сортировки'))

SEX = (
    (1, _('Мальчик')),
    (2, _('Девочка')),
)


class UserProfile(models.Model):
    age = models.IntegerField(_('Возраст'))
    sex = models.IntegerField(choice=SEX, verbose_name=_('Пол'))


class Scool(models.Model):
    name = models.CharField(max_length=40, verbose_name=_('Школа'))
    lat = models.FloatField(verbose_name=_('Широта'))
    lon = models.FloatField(verbose_name=_('Долгота'))

