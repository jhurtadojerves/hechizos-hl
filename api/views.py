from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import SpellSerializer

from spells.models import Spell


class SpellAPIList(ListAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellAPIDetail(RetrieveAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    lookup_field = 'slug'
