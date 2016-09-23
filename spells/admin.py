# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Group, Spell, Range

# Register your models here.

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name',]
    list_editable = ['name',]

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'method', 'object', 'slug',]
    list_editable = ['name', 'type', 'method', 'object',]
    list_filter = ['type',]
    search_fields = ['name',]
    list_per_page = 25

@admin.register(Range)
class RangeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group',]
