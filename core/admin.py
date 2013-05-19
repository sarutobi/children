# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import (
    GroupOfInterest, Interest,
    Organization, Workshop, TimeTable)


class AdminGroupOfInterest(admin.ModelAdmin):
    pass

admin.site.register(GroupOfInterest, AdminGroupOfInterest)


class AdminInterest(admin.ModelAdmin):
    list_display = ('name', 'root')

admin.site.register(Interest, AdminInterest)


class AdminOrganization(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')

admin.site.register(Organization, AdminOrganization)


class TimeTableInline(admin.StackedInline):
    model = TimeTable


class AdminWorkshop(admin.ModelAdmin):
    list_display = ('name', 'organization')
    inlines = [TimeTableInline, ]

admin.site.register(Workshop, AdminWorkshop)
