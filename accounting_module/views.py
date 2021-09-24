from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChartofAccount, JournalEntry
from .serializers import chartofAccountSeralizers, journalEntrySeralizers

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


# ==============================================CHART OF ACCOUNT========================================

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


# this is for litview of chart of account
@api_view(['GET'])
def chart_of_account_list(request):
    """
    This function is for displaying list of chart of Account
    """
    chartofAccount = ChartofAccount.objects.all().order_by('code')
    serializer = chartofAccountSeralizers(chartofAccount, many=True)
    return Response(serializer.data)

# this is for searching chart of account tru ID
@api_view(['GET'])
def getChartofAccount(request,pk):
    """
    This function is for searching chart
    of account for editing putposes
    """
    chartofAccount = ChartofAccount.objects.get(id=pk)
    serializer = chartofAccountSeralizers(chartofAccount, many=False)
    return Response(serializer.data)

# this is to delete chart of account   
@api_view(['DELETE'])
def deleteCOA(request, pk):
    """
    This function is to delete chart of Account
    """
    chartofAccount = ChartofAccount.objects.get(id=pk)
    chartofAccount.delete()
    return Response('data has been removed')

# this is to update chart of account
@api_view(['PUT'])
def update_coa(request, pk):
    data = request.data
    chartofAccounts = ChartofAccount.objects.get(id=pk)
    serializer = chartofAccountSeralizers(instance=chartofAccounts, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# ===========================================JOURNAL ENTRY ================================================

# this is for adding Journal Entries
@api_view(['POST'])
def post_journalEntry(request):
    """
    This function is for creating or to add 
    journal Entry API
    """
    data = request.data
    addChart= JournalEntry.objects.create(
        transdate = data['transdate'],
        journal = data['journal'],
        reference = data['reference'],
        check_no_ref = data['check_no_ref'],
        journalMemo = data['journalMemo'],
        code = data['code'],
        trialBalance_chart = data['trialBalance_chart'],
        account_name = data['account_name'],
        debit = data['debit'], 
        credit = data['credit'],  
        update = data['update'],
        created = data['created'],        
    )
    serializer = journalEntrySeralizers(addChart, many=False)
    return Response(serializer.data)

