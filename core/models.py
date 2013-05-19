# -*- coding: utf-8 -*-

from django.db import models

from users.models import Skill


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


class InteresToSkill(models.Model):
    class Meta:
        verbose_name = 'Рейтинг навыка'
        verbose_name_plural = 'Рейтинги навыков'
        unique_together = (('skill', 'interest'), )

    skill = models.ForeignKey(Skill, verbose_name='Навык')
    interest = models.ForeignKey(Interest, verbose_name='Занятие')
    ratio = models.FloatField(verbose_name='Рейтинг')


DAYS_OF_WEEK = (
    (1, 'Понедельник'),
    (2, 'Вторник'),
    (3, 'Среда'),
    (4, 'Четверг'),
    (5, 'Пятница'),
    (6, 'Суббота'),
    (7, 'Воскресенье'),
)


class TimeTable(models.Model):
    class Meta:
        ordering = ('day', 'start_time')

    day = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name='День недели')
    start_time = models.TimeField(verbose_name='Время начала')
    finish_time = models.TimeField(verbose_name='Время окончания')
    workshop = models.ForeignKey('Workshop')

#    def __unicode__(self):
#        return "%s c %s по %s" % (
#            self.get_day_display(),
#            self.start_time,
#            self.finish_time)


class Organization(models.Model):
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    name = models.CharField(max_length=40, verbose_name='Наименование')
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True)
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефоны',
        blank=True, null=True)

    def __unicode__(self):
        return self.name


class Workshop(models.Model):
    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'

    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=40, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    instructor = models.CharField(max_length=60, verbose_name='Тренер')
    #sheduled = models.ManyToManyField(TimeTable, blank=True, null=True)
    interests = models.ManyToManyField(Interest, verbose_name='Занятия')
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес',
        blank=True, null=True)
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефоны',
        blank=True, null=True)

    def __unicode__(self):
        return "%s: %s" % (self.organization.name, self.name)
