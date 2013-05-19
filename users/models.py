# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserType(models.Model):
    class Meta:
        ordering = ('order',)

    name = models.CharField(max_length=20, verbose_name=_('Наименование'))
    description = models.TextField(
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
    sex = models.IntegerField(choices=SEX, verbose_name=_('Пол'))


class Skill(models.Model):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    name = models.CharField(max_length=30, verbose_name='Навык')
    description = models.TextField(verbose_name='Описание')

    def __unicode__(self):
        return self.name


class Scool(models.Model):
    name = models.CharField(max_length=40, verbose_name=_('Школа'))
    lat = models.FloatField(verbose_name=_('Широта'))
    lon = models.FloatField(verbose_name=_('Долгота'))

