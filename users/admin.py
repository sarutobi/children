# coding: utf-8

from django.contrib import admin

from .models import Skill

class AdminSkill(admin.ModelAdmin):
    pass

admin.site.register(Skill, AdminSkill)
