# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserType(models.Model):
    class Meta:
        order = ('order')

    name = models.CharField(verbose_name=_('Наименование'))
    description = models.Text(
        verbose_name=_('Описание'),
        blank=True,
        null=True)
    icon = models.ImageField()
    order = models.IntegerField(verbose_name=_('Порядок сортировки'))


class UserProfile(models.Model):
    date_of_birth = models.DateField(verbose_name=_('Дата рождения'))
