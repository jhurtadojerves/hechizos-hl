from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import SpellSerializer

from spells.models import Spell, Range


class SpellAPIList(ListAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellAPIDetail(RetrieveAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    lookup_field = 'slug'


class SpellRangeAPIList(ListAPIView):
    serializer_class = SpellSerializer

    def get_queryset(self):
        range = get_object_or_404(Range, slug=self.kwargs['slug'])
        return Spell.objects.filter(range=range, battles=True)