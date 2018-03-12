from django.conf.urls import url

from .views import SpellAPIList, SpellAPIDetail

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

]
