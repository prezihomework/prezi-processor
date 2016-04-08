from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Prezi

from . import views

urlpatterns = [
                url(r'^$', views.index, name='home'),
                url(r'^contact/', views.contact, name='processor/contact.html'),
                url(r'^test/', views.test, name='processor/test.html'),
                url(r'^search/$', views.search),
                url(r'^search/sortByDate', views.sortByDate),
                url(r'^search/(?P<keyword>[a-zA-Z0-9 ]+)$', views.search),
                url(r'^list/', views.list, name='processor/list.html'),
                url(r'^deserialize/', views.deserialize, name='processor/deserialize.html'),
]
