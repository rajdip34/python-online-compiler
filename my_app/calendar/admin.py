from django.contrib import admin
from .models import *
from datetime import datetime





class CalendarAdmin(admin.ModelAdmin):
    #list_display = ["username", "company", "firstname", "lastname"]
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

admin.site.register(Calendar,CalendarAdmin)
