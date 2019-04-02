import json
from my_app.country.utils import CountryUtils

import json
from my_app.currency.models import Currency

import json
import pandas as pd

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
from .models import Country
from .serializers import CountrySerializer


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


@api_view(http_method_names=["GET"])
@login_required
def get_country_list(request):
    _countryUtils = CountryUtils()
    rows = _countryUtils.getList()
    jsondata = []
    for index, row in rows.iterrows():
        t = {
            "name": row['name'],
            "id": row['id']
        }
        jsondata.append(t)
    return Response({"results": jsondata})


@api_view(http_method_names=["GET"])
@login_required
def country_details_for_company(request, name):
    _countryUtils = CountryUtils()
    rows = _countryUtils.getCountryforCompany(name)
    jsondata = []
    for row in rows:
        t = {
            "name": row.countryid.name if row.countryid else "",
        }
        jsondata.append(t)
    return Response({"results": jsondata})

"""
import yaml
import os
DIR_NAME = os.path.abspath(os.path.dirname(__file__))


country_view = Blueprint('country_view', __name__)


@country_view.route('/Country/<string:name>/', methods=['GET'])
@swag_from('country_name.yml')
def CountryPerCountry(name):
    _countryUtils = CountryUtils()
    rows = _countryUtils.getCountryforCompany(name)
    jsondata = []
    for row in rows:
        t = {
        "name" : row[0],
        }
        jsondata.append(t)        
    return jsonify({'results':jsondata})


@country_view.route('/Country',methods=['GET'])
@swag_from('country.yml')
def getList():

    _countryUtils = CountryUtils()
    rows = _countryUtils.getList()
    
    jsondata = []
    for row in rows:
        t = {
        "name" : row[0],
        }
        jsondata.append(t)        
    return jsonify({'results':jsondata})
"""