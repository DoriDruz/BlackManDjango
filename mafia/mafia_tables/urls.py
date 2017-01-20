from django.conf.urls import url

from mafia_tables import views
from .models import *

app_name = 'mafia_tables'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<BusinessType_id>[0-9]+)/$', views.detail, name='detail'),
]
