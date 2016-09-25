from django.conf.urls import url
from django.contrib import admin

from .views import (SpellDetailView, 
                    SpellListView, 
                    SpellSearchView,
                    SpellCategoryListView,
                    SpellEditView,
                    SpellListRangeView,)

app_name = 'Spell'
urlpatterns = [
    url(r'^$', SpellListView.as_view(), name='spell_list'),
    url(r'^all/$', SpellListView.as_view(), name='spell_list'),
    url(r'^(?P<slug>[-\w ]+)/$', SpellCategoryListView.as_view(), name='spell_category'),
    url(r'^search/$', SpellSearchView.as_view() ,name='spell_search'),
    url(r'^hechizo/(?P<slug>[-\w ]+)/$', SpellDetailView.as_view(), name='spell_detail'),
    url(r'^hechizo/(?P<slug>[-\w ]+)/edit/$', SpellEditView.as_view(), name='spell_edit'),
    url(r'^(?P<slug>[-\w ]+)/(?P<slug_range>[-\w ]+)$', SpellListRangeView.as_view(), name='spell_range'),
]