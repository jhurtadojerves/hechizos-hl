from django.conf.urls import url
from django.contrib import admin

from .views import SpellListView, SpellSearchView

app_name = 'Spell'
urlpatterns = [
    url(r'^$', SpellListView.as_view(), name='spell_list'),
    url(r'^buscar/$', SpellSearchView.as_view() ,name='spell_search'),
]