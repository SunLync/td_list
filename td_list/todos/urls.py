from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details)
]