from rest_framework import serializers
from .models import Calendarholiday

class CalendarholidaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendarholiday
        fields = '__all__'
        read_only_fields = ('modifyuserid', 'modifydatetime')