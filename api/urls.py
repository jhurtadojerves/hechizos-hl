from django.conf.urls import url
from django.urls import path

from .views import SpellAPIList, SpellAPIDetail, SpellRangeAPIList, CategoryAPIList, RangeCategoryAPIList, SpellRangeCategoryAPIList

app_name = 'Api'

urlpatterns = [
    url(
        regex='^categories/$',
        view=CategoryAPIList.as_view(),
        name='category-list'
    ),
    url(
        regex='^categories/(?P<slug>[-\w]+)/$',
        view=RangeCategoryAPIList.as_view(),
        name='category-detail'
    ),
    url(
        regex='^categories/(?P<slug_category>[-\w]+)/(?P<slug>[-\w]+)/$',
        view=SpellRangeCategoryAPIList.as_view(),
        name='category-range-detail'
    ),
    url(
        regex='^spells/$',
        view=SpellAPIList.as_view(),
        name='list'
    ),
    url(
        regex='^spells/(?P<slug>[-\w]+)/$',
        view=SpellAPIDetail.as_view(),
        name='detail'
    ),
    url(
        regex='^range/(?P<slug>[-\w]+)/$',
        view=SpellRangeAPIList.as_view(),
        name='list_by_range'
    ),


]
