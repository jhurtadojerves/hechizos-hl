from import_export import resources, fields
from import_export.admin import ImportExportMixin
from .models import Group, Spell, Range


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        fields = ['id', 'name', 'slug', ]
        import_order = fields
        export_order = fields
        IMPORT_EXPORT_SKIP_ADMIN_LOG = True


class SpellResource(resources.ModelResource):
    class Meta:
        model = Spell
        fields = ['id', 'name', 'slug', 'description', 'range', 'type', 'method', 'object', 'battles', ]
        import_order = fields
        export_order = fields
        IMPORT_EXPORT_SKIP_ADMIN_LOG = True


class RangeResource(resources.ModelResource):
    class Meta:
        model = Range
        fields = ['id', 'name', 'group', 'slug', ]
        import_order = fields
        export_order = fields
        IMPORT_EXPORT_SKIP_ADMIN_LOG = True