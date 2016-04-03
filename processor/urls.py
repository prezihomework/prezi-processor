from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^text/', views.text, name='text'),
               url(r'^base$', views.base, name='base'),
]
