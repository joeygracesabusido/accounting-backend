from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChartofAccount
from .serializers import chartofAccountSeralizers

from rest_framework import generics

from rest_framework.parsers import JSONParser

# import django_filters.rest_framework

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from datetime import datetime


from rest_framework import generics
from rest_framework import filters


@api_view(['GET'])
def getRoutes(request):
    return Response('Our Api')

# this is for adding chart of account
@api_view(['POST'])
def post_chartofaccount(request):
    """
    This function is for creating or to add 
    chart of Account API
    """
    data = request.data
    addChart= ChartofAccount.objects.create(
        trialBalance_chart=data['trialBalance_chart'],
        account_name=data['account_name'],
        code=data['code']
    )
    serializer = chartofAccountSeralizers(addChart, many=False)
    return Response(serializer.data)

    # serializer = chartofAccountSeralizers(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)