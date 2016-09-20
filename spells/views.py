# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template.context import RequestContext
from django.http import JsonResponse

from django.views.generic import DetailView, ListView, View

from .models import Spell, Group


class SpellListView(ListView):
    model = Spell
    template_name = 'spells/spell_list.html'
    context_object_name = 'spells'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(SpellListView, self).get_context_data(**kwargs)
        context['categories'] = Group.objects.all()
        return context


class SpellSearchView(View):
    model = Spell

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            spells = self.model.objects.filter(name__istartswith=request.GET['name']).values('id', 'name', 'slug')
            return JsonResponse(list(spells), safe=False)
        return JsonResponse("Solo se permiten consultas mediante AJAX", safe=False)

class SpellDetailView(DetailView):
    model = Spell
    template_name = 'spells/spell_detail.html'
    slug_field = 'slug'
    context_object_name = 'spell'

    def get_context_data(self, **kwargs):
        context = super(SpellDetailView, self).get_context_data(**kwargs)
        context['categories'] = Group.objects.all()
        return context

class SpellCategoryListView(SpellListView):

    def get_queryset(self):
        group = get_object_or_404(Group, id = self.args[0])
        queryset = self.model.objects.filter(group = group)
        return queryset