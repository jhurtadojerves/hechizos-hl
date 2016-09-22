from django.conf.urls import url
from django.contrib import admin

from .views import (SpellDetailView, 
                    SpellListView, 
                    SpellSearchView,
                    SpellCategoryListView,
                    SpellEditView,)

app_name = 'Spell'
urlpatterns = [
    url(r'^$', SpellListView.as_view(), name='spell_list'),
    url(r'^all/$', SpellListView.as_view(), name='spell_list'),
    url(r'^grupo/([0-9]+)/$', SpellCategoryListView.as_view(), name='spell_category'),
    url(r'^search/$', SpellSearchView.as_view() ,name='spell_search'),
    url(r'^(?P<slug>[-\w ]+)/$', SpellDetailView.as_view(), name='spell_detail'),
    url(r'^(?P<slug>[-\w ]+)/edit/$', SpellEditView.as_view(), name='spell_edit'),
]