from django.shortcuts import render
from django.views.generic import ListView

from .models import Spell, Group

class SpellListView(ListView):
    model = Spell
    template_name = 'spells/spell_list.html'
    context_object_name = 'spells'