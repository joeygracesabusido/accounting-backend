from django.db import models
from django.db.models import fields
from rest_framework.relations import ManyRelatedField
from rest_framework.serializers import ModelSerializer
from .models import ChartofAccount, JournalEntry
from rest_framework import serializers

class chartofAccountSeralizers(ModelSerializer):
    class Meta:
        model = ChartofAccount
        fields = '__all__'


# =====================================JOURNAL ENTRY ====================================

class journalEntrySeralizers(ModelSerializer):
    # account_name = serializers.SerialMethodSerializer(many=True,read_only=True)
    # account_name = serializers.SerialMethodSerializer()
    # def get_account_name(obj):
    #     return chartofAccountSeralizers(obj.account_name).data

    # marks = chartofAccountSeralizers(many=True, 
    #                                 read_only=True)

    # marks = chartofAccountSeralizers(many=True, 
    #                                 read_only=True)
    
    class Meta:
        model = JournalEntry
        fields = '__all__'