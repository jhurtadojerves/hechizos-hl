from django.conf.urls import url

from .views import (
    SpellDetailView,
    SpellListView,
    SpellSearchView,
    SpellCategoryListView,
    SpellEditView,
    SpellListRangeView,
)


app_name = 'Spell'
urlpatterns = [
    url(
        regex='^$',
        view=SpellListView.as_view(),
        name='spell_list'
    ),
    url(
        regex='^rol/$',
        view=SpellListView.as_view(rol=True),
        name='spell_list_rol'
    ),
    url(
        regex='^search/$',
        view=SpellSearchView.as_view(),
        name='spell_search'
    ),
    url(
        regex='^(?P<slug>[-\w]+)/$',
        view=SpellCategoryListView.as_view(),
        name='spell_category'
    ),
    url(
        regex='^rol/(?P<slug>[-\w]+)/$',
        view=SpellCategoryListView.as_view(rol=True),
        name='spell_category_rol'
    ),
    url(
        regex='^spell/(?P<slug>[-\w]+)/$',
        view=SpellDetailView.as_view(),
        name='spell_detail'
    ),
    url(
        regex='^spell/(?P<slug>[-\w]+)/edit/$',
        view=SpellEditView.as_view(),
        name='spell_edit'
    ),
    url(
        regex='^(?P<slug>[-\w]+)/(?P<slug_range>[-\w]+)/$',
        view=SpellListRangeView.as_view(rol=False),
        name='spell_range'
    ),
    url(
        regex='^rol/(?P<slug>[-\w]+)/(?P<slug_range>[-\w]+)/',
        view=SpellListRangeView.as_view(rol=True),
        name='spell_range_rol'
    ),
]
