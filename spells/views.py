# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.context import RequestContext
from django.http import JsonResponse

from django.views.generic import ListView

from .models import Spell, Group

class SpellListView(ListView):
    model = Spell
    template_name = 'spells/spell_list.html'
    context_object_name = 'spells'

def home(request):
	return render(request, 'search.html', {}, context_instance=RequestContext(request))

def buscar(request):
	if request.is_ajax():
		spells = Spell.objects.filter(name__istartswith=request.GET['name']).values('id', 'name', 'slug')
		return JsonResponse(list(spells), safe=False)
	return JsonResponse("Solo se permiten consultas mediante AJAX", safe=False)

