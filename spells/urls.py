from django.conf.urls import url
from django.contrib import admin

from .views import (SpellDetailView, 
                    SpellListView, 
                    SpellSearchView, 
                    SpellFenixListView, 
                    SpellMarcaListView, 
                    SpellLibrosListView)

app_name = 'Spell'
urlpatterns = [
    url(r'^$', SpellListView.as_view(), name='spell_list'),
    url(r'^all/$', SpellListView.as_view(), name='spell_list'),
    url(r'^fenix/$', SpellFenixListView.as_view(), name='spell_orden'),
    url(r'^mortifagos/$', SpellMarcaListView.as_view(), name='spell_marca'),
    url(r'^libros/$', SpellLibrosListView.as_view(), name='spell_libros'),
    url(r'^search/$', SpellSearchView.as_view() ,name='spell_search'),
    url(r'^(?P<slug>[-\w ]+)/$', SpellDetailView.as_view(), name='spell_detail'),
]