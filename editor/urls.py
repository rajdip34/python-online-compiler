
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings

from editor.views import *


from rest_framework import routers

urlpatterns = [
    url(r'^$', index),
    url(r'^nav_updater', nav_updater),
    url(r'^nav_folder', nav_folder),
    url(r'^python_libs_js', python_libs_js),
    url(r'^chartdata', chartdata),
    url(r'^commander', commander),

]