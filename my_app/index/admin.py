from django.contrib import admin
from my_app.index.models import *
from datetime import datetime


"""
from django.contrib import admin

def auto_register(model):
    #Get all fields from model, but exclude autocreated reverse relations
    field_list = [f.name for f in model._meta.get_fields() if f.auto_created == False]
    # Dynamically create ModelAdmin class and register it.
    my_admin = type('MyAdmin', (admin.ModelAdmin,),
                        {'list_display':field_list }
                        )
    try:
        admin.site.register(model,my_admin)
    except Exception as e:
        # This model is already registered
        print(e)

from django.apps import apps
for model in apps.get_app_config('main').get_models():
    auto_register(model)
"""

class IndexAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Index._meta.get_fields() if f.auto_created == False]
    #filter_horizontal = ('site',)
    exclude = ["modifyuser", "modifydatetime"]

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        """ to check that admin of egcs can not have 5 account """
        obj.modifyuser = request.user
        obj.modifydatetime = datetime.now()
        obj.save()

admin.site.register(Index,IndexAdmin)


