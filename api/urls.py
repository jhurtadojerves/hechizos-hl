from django.conf.urls import url

from .views import SpellAPIList, SpellAPIDetail, SpellRangeAPIList

app_name = 'Api'

urlpatterns = [
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
