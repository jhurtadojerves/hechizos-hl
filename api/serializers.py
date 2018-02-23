from rest_framework import serializers

from spells.models import Spell


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = "__all__"
