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
from .models import Currency
from .serializers import CurrencySerializer

class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


@login_required
def home(request):
    context = {}
    return HttpResponse("Welcome to the Currency Home.")


@api_view(http_method_names=["GET"])
@login_required
def currencyView(request, id=None, page=1):
    page = request.GET.get("page", 1)
    if not id or not id.isdigit():
        currencies = Currency.objects.all()
    elif id and id.isdigit() and int(id) > 0:
        currencies = Currency.objects.filter(id=id)
    try:
        paginator = Paginator(currencies, 1000)
        currencies = paginator.page(page)
    except PageNotAnInteger:
        currencies = paginator.page(1)
    except EmptyPage:
        currencies = paginator.page(paginator.num_pages)

    if not currencies:
        raise Http404("No Currency Model matches the given query.")
    res = {}
    for currency in currencies:
        res[currency.id] = {
            'name': currency.name,
            'description': currency.description,
            'modifyuserid': currency.modifyuserid_id,
            'modifydatetime': str(currency.modifydatetime),
        }
    return Response(res)
"""
import yaml
import os
DIR_NAME = os.path.abspath(os.path.dirname(__file__))
 
currency = Blueprint('currency', __name__)
 
@currency.route('/currency')
def home():
    return "Welcome to the currency Home."



@currency.route('/currency/', methods=['GET'])
@currency.route('/currency/<int:id>/', methods=['GET'])
@swag_from('currency_view.yml')
def currencyView(id=None, page=1):
    if not id:
        currencies = Currency.query.paginate(page, 1000).items
    elif id > 0:
        currencies = Currency.query.filter(Currency.id == id).all()

    if not currencies:
        abort(404)
    res = {}
    for currency in currencies:
        res[currency.id] = {
            'name': currency.name,
            'description': currency.description,
            'modifyuserid': currency.modifyuserid,
            'modifydatetime': str(currency.modifydatetime),
        }
    return jsonify(res)
"""
