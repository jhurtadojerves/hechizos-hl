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
    template_name = 'spells/spell_list.html'
    context_object_name = 'spells'
    paginate_by = 5

    def get_queryset(self):
        if self.rol:
            queryset = self.model.objects.exclude(battles = True)
        else:
            queryset = self.model.objects.exclude(battles = False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SpellListView, self).get_context_data(**kwargs)
        context['categories'] = Group.objects.all().order_by('id')
        context['ranges'] = Range.objects.all().order_by('id')
        context['rol'] = self.rol

        return context

class SpellSearchView(View):
    model = Spell
    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            spells = self.model.objects.filter(name__icontains = request.GET['name']).values('id', 'name', 'slug')[:10]
            return JsonResponse(list(spells), safe=False)
        return JsonResponse("Solo se permiten consultas mediante AJAX", safe=False)

class SpellDetailView(DetailView):
    model = Spell
    template_name = 'spells/spell_detail.html'
    slug_field = 'slug'
    context_object_name = 'spell'
    order_by = 'range'

    def get_context_data(self, **kwargs):
        context = super(SpellDetailView, self).get_context_data(**kwargs)
        context['categories'] = Group.objects.all().order_by('id')
        context['ranges'] = Range.objects.all().order_by('id')
        return context

class SpellCategoryListView(SpellListView):
    def get_queryset(self):
        group = get_object_or_404(Group, slug = self.kwargs['slug'])
        ranges = Range.objects.filter(group = group)
        if self.rol:
            queryset = self.model.objects.filter(range__in=ranges).exclude(battles = True)
        else:
            queryset = self.model.objects.filter(range__in=ranges).exclude(battles = False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SpellCategoryListView, self).get_context_data(**kwargs)
        context['categories'] = Group.objects.all().order_by('id')
        context['ranges'] = Range.objects.all().order_by('id')
        context['category'] = get_object_or_404(Group, slug = self.kwargs['slug'])
        context['flag'] = True
        return context

class SpellEditView(UpdateView):
    model = Spell
    fields = ['name', 'description', 'range', 'type', 'method', 'object',]
    template_name_suffix = '_update'
    success_url = '../'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SpellEditView, self).dispatch(*args, **kwargs)

class SpellListRangeView(SpellListView):

    def get_queryset(self):
        group = get_object_or_404(Group, slug = self.kwargs['slug'])
        range = get_object_or_404(Range, slug = self.kwargs['slug_range'])

        if self.rol:
            queryset = self.model.objects.filter(range = range, battles = False)
        else:
            queryset = self.model.objects.filter(range=range, battles = True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SpellListRangeView, self).get_context_data(**kwargs)
        context['categories'] = Group.objects.all().order_by('id')
        context['ranges'] = Range.objects.all().order_by('id')
        context['category'] = get_object_or_404(Group, slug=self.kwargs['slug'])
        context['flag'] = True
        context['rol'] = self.rol
        return context