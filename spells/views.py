# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template.context import RequestContext
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, View, UpdateView

from .models import Spell, Group, Range


class SpellListView(ListView):
    rol = False
    model = Spell
    template_name = "spells/spell_list.html"
    context_object_name = "spells"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SpellListView, self).get_context_data(**kwargs)
        context.update(
            {
                "categories": Group.objects.all().order_by("id"),
                "ranges": Range.objects.all().order_by("id"),
                "rol": self.rol,
            }
        )
        return context


class SpellSearchView(View):
    model = Spell

    def get(self, request, *args, **kwargs):
        spells = self.model.objects.filter(name__icontains=request.GET["name"]).values(
            "id", "name", "slug"
        )[:10]
        return JsonResponse(list(spells), safe=False)


class SpellDetailView(DetailView):
    model = Spell
    template_name = "spells/spell_detail.html"
    slug_field = "slug"
    context_object_name = "spell"
    order_by = "range"

    def get_context_data(self, **kwargs):
        context = super(SpellDetailView, self).get_context_data(**kwargs)
        context.update(
            {
                "categories": Group.objects.all().order_by("id"),
                "ranges": Range.objects.all().order_by("id"),
            }
        )
        return context


class SpellCategoryListView(SpellListView):
    def get_queryset(self):
        group = get_object_or_404(Group, slug=self.kwargs["slug"])
        ranges = Range.objects.filter(group=group)
        queryset = self.model.objects.filter(range__in=ranges)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SpellCategoryListView, self).get_context_data(**kwargs)
        context.update(
            {
                "categories": Group.objects.all().order_by("id"),
                "ranges": Range.objects.all().order_by("id"),
                "category": get_object_or_404(Group, slug=self.kwargs["slug"]),
                "flag": True,
            }
        )

        return context


class SpellEditView(UpdateView):
    model = Spell
    fields = [
        "name",
        "description",
        "range",
        "type",
        "method",
        "object",
    ]
    template_name_suffix = "_update"
    success_url = "../"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SpellListRangeView(SpellListView):
    def get_queryset(self):
        group = get_object_or_404(Group, slug=self.kwargs["slug"])
        group_range = get_object_or_404(Range, slug=self.kwargs["slug_range"])

        queryset = self.model.objects.filter(range=group_range)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "categories": Group.objects.all().order_by("id"),
                "ranges": Range.objects.all().order_by("id"),
                "category": get_object_or_404(Group, slug=self.kwargs["slug"]),
                "flag": True,
                "rol": self.rol,
            }
        )
        return context
