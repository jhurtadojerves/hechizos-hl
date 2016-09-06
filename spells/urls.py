from django.conf.urls import url
from django.contrib import admin

from .views import SpellListView

app_name = 'Spell'
urlpatterns = [
    url(r'^', SpellListView.as_view(), name='spell_list'),
]