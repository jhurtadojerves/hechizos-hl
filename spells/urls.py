from django.urls import path
from django.contrib import admin

from .views import (SpellDetailView, 
                    SpellListView, 
                    SpellSearchView,
                    SpellCategoryListView,
                    SpellEditView,
                    SpellListRangeView,)

app_name = 'Spell'
urlpatterns = [
    path('', SpellListView.as_view(), name='spell_list'),
    path('rol/', SpellListView.as_view(rol=True), name='spell_list_rol'),
    path('search/', SpellSearchView.as_view(), name='spell_search'),
    path('<slug:slug>/', SpellCategoryListView.as_view(), name='spell_category'),
    path('rol/<slug:slug>/', SpellCategoryListView.as_view(rol=True), name='spell_category_rol'),
    path('spell/<slug:slug>/', SpellDetailView.as_view(), name='spell_detail'),
    path('spell/<slug:slug>/edit/', SpellEditView.as_view(), name='spell_edit'),
    path('<slug:slug>/<slug:slug_range>/', SpellListRangeView.as_view(rol=False), name='spell_range'),
    path('rol/<slug:slug>/<slug:slug_range>/', SpellListRangeView.as_view(rol=True), name='spell_range_rol'),
]