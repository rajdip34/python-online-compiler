from rest_framework import serializers
from .models import Index

class indexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = "__all__"
        read_only_fields = ('modifyuser', 'modifydatetime')
        #fields = ('id','name','currencyid','bloombergticker','reutersric',
        #          'bloombergid','indextypeid','indexcategoryid','indexfamilyid','modifyuser',
        #          'modifydatetime','active','customindex','customindexconfiguration')




    