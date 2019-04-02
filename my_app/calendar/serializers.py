from rest_framework import serializers
from .models import Calendar

class CalenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = '__all__'
        read_only_fields = ('modifyuserid', 'modifydatetime')