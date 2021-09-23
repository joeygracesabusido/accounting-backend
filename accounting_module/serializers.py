from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import ChartofAccount

class chartofAccountSeralizers(ModelSerializer):
    class Meta:
        model = ChartofAccount
        fields = '__all__'