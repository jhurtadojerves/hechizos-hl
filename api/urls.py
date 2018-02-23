from django.conf.urls import url

from .views import SpellAPIList

app_name = 'Api'

urlpatterns = [
    url(
        regex='^',
        view=SpellAPIList.as_view(),
        name='list'
    ),

]
