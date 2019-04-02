
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from my_app.country.views import *

from rest_framework import routers

country_routers = routers.DefaultRouter()
country_routers.register('country', CountryView)


urlpatterns = [
    url(r'^Country/$', get_country_list, name="country"),
    url(r'^Country/(?P<name>[\w ]+)/$', country_details_for_company, name="country_details_for_company"),
]