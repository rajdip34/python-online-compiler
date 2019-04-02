from django.conf.urls import include, url
# import django.path as path
from my_app.index.views import *
from rest_framework import routers

index_routers = routers.DefaultRouter()
index_routers.register('index', IndexView)


from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    # url(r'^web/$', index_web, name="index_web"),
    # url(r'^customweb/$', index_customweb, name="index_customweb"),
    url(r'^index/$', IndexView, name="IndexView"),
    url(r'^index/(?P<id>\d+)/$', IndexView, name="IndexView_indexId"),
]