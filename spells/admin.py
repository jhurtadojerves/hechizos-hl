# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Group, Spell

# Register your models here.

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name',]
    list_editable = ['name',]

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'range', 'type', 'method', 'object', 'slug',]
    list_editable = ['name', 'type', 'method', 'object',]
    list_filter = ['group', 'range', 'type',]
    search_fields = ['group__name', 'range', 'name',]
    list_per_page = 25


