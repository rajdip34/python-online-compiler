import json


from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest, \
                        HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import CalendarholidaySerializer
from my_app.calendarholiday.utils import calendarHolidayUtils
from my_app.calendarholiday.models import Calendarholiday


class CalendarholidayView(viewsets.ModelViewSet):
    queryset = Calendarholiday.objects.all()
    serializer_class = CalendarholidaySerializer


@api_view(http_method_names=["GET"])
@login_required
def getCalendarHoliday(request, calendarid, startDate=None, endDate=None):
    _calendarHolidayUtils = calendarHolidayUtils(calendarid)
    results = _calendarHolidayUtils.getCalendarHolidays()
    return Response(results.to_dict('records'))


@api_view(http_method_names=["GET"])
@login_required
def getCalendarHolidayRange(request, calendarid, startDate, endDate):
    _calendarHolidayUtils = calendarHolidayUtils(calendarid)
    results = _calendarHolidayUtils.getCalendarHolidaysRange(startDate, endDate)
    return Response(results.to_dict('records'))
