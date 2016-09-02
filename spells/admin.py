# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Type, Spell
# Register your models here.

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['id','name',]
	list_editable = ['name',]

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'type', 'range',]
	list_editable = ['name',]
	list_filter = ['type', 'range',]
	search_fields = ['type__name', 'range', 'name']


