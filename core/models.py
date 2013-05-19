# -*- coding: utf-8 -*-

from django.db import models


class GroupOfInterest(models.Model):
    class Meta:
        verbose_name = 'Группа интересов'
        verbose_name_plural = 'Группы интересов'

    name = models.CharField(max_length=40, verbose_name=('Наименование'))
#    icon = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Interest(models.Model):
    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    name = models.CharField(max_length=40, verbose_name=('Наименование'))
    root = models.ForeignKey(GroupOfInterest)
#    icon = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.name

