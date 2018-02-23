from rest_framework import serializers

from spells.models import Spell


class SpellSerializer:

    class Meta:
        model = Spell
        fields = (
            'name',
            'description',
            'type',
            'method',
            'object',
        )
