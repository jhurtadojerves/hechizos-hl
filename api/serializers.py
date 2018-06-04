from rest_framework import serializers

from spells.models import Spell, Range


class RangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Range
        fields = ('name',)


class SpellSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="Api:detail", lookup_field="slug")
    type = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()
    object = serializers.SerializerMethodField()
    range = RangeSerializer(many=True, read_only=True)

    class Meta:
        model = Spell
        fields = (
            'url',
            'id',
            'name',
            'description',
            'range',
            'type',
            'method',
            'object',
            'battles'
        )

    def get_type(self, obj):
        return obj.get_type_display()

    def get_method(self, obj):
        return obj.get_method_display()

    def get_object(self, obj):
        return obj.get_object_display()
