from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Prezi

from . import views

urlpatterns = [
                url(r'^$', views.index, name='home'),
                url(r'^contact/', views.contact, name='processor/contact.html'),
                url(r'^test/', views.test, name='processor/test.html'),
                url(r'^search/$', ListView.as_view(
                                    queryset=Prezi.objects.all(),
                                    template_name="processor/search.html")),
                url(r'^search/sortByDate', ListView.as_view(
                    queryset=Prezi.objects.all().order_by('pub_date'),
                    template_name="processor/search.html")),
                url(r'^list/', views.list, name='processor/list.html'),
                url(r'^deserialize/', views.deserialize, name='processor/deserialize.html'),
]
