from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import ChartofAccount, JournalEntry

class chartofAccountSeralizers(ModelSerializer):
    class Meta:
        model = ChartofAccount
        fields = '__all__'


# =====================================JOURNAL ENTRY ====================================

class journalEntrySeralizers(ModelSerializer):

    class Meta:
        model = JournalEntry
        fields = '__all__'