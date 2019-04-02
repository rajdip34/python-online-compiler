from django.conf.urls import include, url
from .views import *
from rest_framework import routers

calendar_routers = routers.DefaultRouter()
calendar_routers.register('calendar', CalendarView)


urlpatterns = [

 ]