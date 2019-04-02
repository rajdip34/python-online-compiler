from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    #modifyuserid = serializers.ReadOnlyField(source='Currency.modifyuserid')
    #modifydatetime = serializers.ReadOnlyField(source='Currency.modifyuserid')

    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ('modifyuserid', 'modifydatetime')