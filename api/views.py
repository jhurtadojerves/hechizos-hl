from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import SpellSerializer

from spells.models import Spell


class SpellAPIList(ListAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
