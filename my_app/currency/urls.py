from django.conf.urls import include, url
from .views import *
from rest_framework import routers

currency_routers = routers.DefaultRouter()
currency_routers.register('currency', CurrencyView)


urlpatterns = [
     #url(r'^currency/$', currencyView, name="currency"),
     url(r'^currency/(?P<id>\d+)/$', currencyView, name="currency_id"),

 ]