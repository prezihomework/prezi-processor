from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Prezi

from . import views

urlpatterns = [
               url(r'^$', views.index, name='home'),
               url(r'^contact/', views.contact, name='processor/contact.html'),
               url(r'^search/', ListView.as_view(
                                    queryset=Prezi.objects.all(),
                                    template_name="processor/search.html")),
]
