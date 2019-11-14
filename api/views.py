from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .pagination import SpellsPagination, RangePagination
from .serializers import SpellSerializer, RangeSerializer, CategorySerializer

from spells.models import Spell, Range, Group


class SpellAPIList(ListAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    pagination_class = SpellsPagination


class SpellAPIDetail(RetrieveAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    lookup_field = 'slug'


class SpellRangeAPIList(ListAPIView):
    serializer_class = SpellSerializer

    def get_queryset(self):
        range = get_object_or_404(Range, slug=self.kwargs['slug'])
        return Spell.objects.filter(range=range, battles=True)


class CategoryAPIList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Group.objects.all()
    pagination_class = RangePagination


class RangeCategoryAPIList(ListAPIView):
    serializer_class = RangeSerializer
    pagination_class = RangePagination

    def get_queryset(self):
        category = get_object_or_404(Group, slug=self.kwargs['slug'])
        return Range.objects.filter(group=category)


class SpellRangeCategoryAPIList(ListAPIView):
    serializer_class = SpellSerializer
    pagination_class = SpellsPagination

    def get_queryset(self):
        range_ = get_object_or_404(Range, slug=self.kwargs['slug'])
        return Spell.objects.filter(range=range_)
