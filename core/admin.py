# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import GroupOfInterest, Interest


class AdminGroupOfInterest(admin.ModelAdmin):
    pass


class AdminInterest(admin.ModelAdmin):
    pass

admin.site.register(GroupOfInterest, AdminGroupOfInterest)
admin.site.register(Interest, AdminInterest)
