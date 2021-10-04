from django.contrib import admin
from .models import Group, Spell, Range
from .resources import GroupResource, SpellResource, RangeResource, ImportExportMixin


@admin.register(Group)
class GroupAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
    ]
    list_editable = [
        "name",
    ]
    class_source = GroupResource


@admin.register(Spell)
class SpellAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "type",
        "method",
        "object",
        "slug",
    ]
    list_editable = [
        "name",
        "type",
        "method",
        "object",
    ]
    list_filter = [
        "type",
        "range__group",
        "range",
    ]
    search_fields = [
        "name",
    ]
    list_per_page = 25
    class_source = SpellResource


@admin.register(Range)
class RangeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "group",
        "group",
        "slug",
    ]
    class_source = RangeResource
