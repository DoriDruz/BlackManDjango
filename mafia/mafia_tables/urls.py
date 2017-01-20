from django.conf.urls import url

from mafia_tables import views

app_name = 'mafia_tables'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
