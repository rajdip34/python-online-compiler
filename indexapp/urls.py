"""indexapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.staticfiles import views as sviews
from my_app.index.views import *
from my_app.index.views import IndexView as Home


from my_app.index.urls import index_routers
from my_app.currency.urls import currency_routers
from my_app.calendar.urls import calendar_routers
from my_app.calendarholiday.urls import calendarholiday_routers
from my_app.country.urls import country_routers



from rest_framework import routers

base_router = routers.DefaultRouter()
base_router.registry.extend(index_routers.registry)
base_router.registry.extend(currency_routers.registry)
base_router.registry.extend(calendar_routers.registry)
base_router.registry.extend(calendarholiday_routers.registry)
base_router.registry.extend(calendar_routers.registry)



urlpatterns = [
    url(r'^editor/',  include('editor.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),

]
#urlpatterns += base_router.urls



if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', sviews.serve),
    ]