from django.conf.urls import include, url
from .views import *
from rest_framework import routers
from my_app.calendarholiday.views import CalendarholidayView

calendarholiday_routers = routers.DefaultRouter()
calendarholiday_routers.register('calendarholiday', CalendarholidayView)


urlpatterns = [
    url(r'^calendar/(?P<calendarid>\w+)/holiday/$', getCalendarHoliday, name="getIndexDivisor"),
    url(r'^calendar/(?P<calendarid>\w+)/holiday/(?P<startDate>\d{4}-\d{2}-\d{2})/(?P<endDate>\d{4}-\d{2}-\d{2})/$', getCalendarHolidayRange, name="getIndexDivisor_enddate"),

]