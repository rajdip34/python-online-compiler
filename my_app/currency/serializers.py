from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    #modifyuserid = serializers.ReadOnlyField(source='Currency.modifyuserid')
    #modifydatetime = serializers.ReadOnlyField(source='Currency.modifyuserid')

    class Meta:
        model = Currency
        fields = ('id','name','modifyuserid','modifydatetime')
        read_only_fields = ('modifyuserid', 'modifydatetime')