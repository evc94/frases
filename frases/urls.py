from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^frase/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^frase/new/$', views.post_new, name='post_new'),
    url(r'^frase/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^frase/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
]
