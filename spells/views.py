# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template.context import RequestContext
from django.http import JsonResponse
from models import Spell

# Create your views here.

def home(request):
	return render(request, 'search.html', {}, context_instance=RequestContext(request))

def buscar(request):
	if request.is_ajax():
		spells = Spell.objects.filter(name__istartswith=request.GET['name']).values('id', 'name', 'slug')
		return JsonResponse(list(spells), safe=False)
	return JsonResponse("Solo se permiten consultas mediante AJAX", safe=False)