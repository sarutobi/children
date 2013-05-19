# coding: utf-8

from django.contrib import admin

from .models import Skill
from core.models import InteresToSkill


class AdminSkillRating(admin.TabularInline):
    model = InteresToSkill


class AdminSkill(admin.ModelAdmin):
    inlines = [AdminSkillRating, ]

admin.site.register(Skill, AdminSkill)
