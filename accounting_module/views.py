from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChartofAccount, JournalEntry
from .serializers import chartofAccountSeralizers, journalEntrySeralizers


from rest_framework.views import APIView
from rest_framework import viewsets

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

# # this is for adding Journal Entries
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
        account_name = data ['account_name'],
        debit = data['debit'], 
        credit = data['credit'],  
           
    )

    serializer = journalEntrySeralizers(addChart, many=False)
    return Response(serializer.data)

# this is for adding Journal Entries
# @api_view(['POST'])
# def post_journalEntry(request):
#     """
#     This function is for creating or to add 
#     journal Entry API
#     """
#     data = request.data
#     if request.method =="POST":
#         transdate = request.POST.get('transdate'),
#         journal = request.POST.get('journal'),
#         reference = request.POST.get('reference'),
#         check_no_ref = request.POST.get('check_no_ref'),
#         journalMemo = request.POST.get('journalMemo'),
#         account_name_id = request.POST.get('accountName'),
#         account_name = ChartofAccount.objects.get(account_name=account_name_id),
#         debit = request.POST.get('debit'), 
#         credit = request.POST.get('credit')  

#         addChart= JournalEntry.objects.create(
#             transdate = data[transdate],
#             journal =  data[journal],
#             reference =  data[reference],
#             check_no_ref =  data[check_no_ref],
#             journalMemo =  data[journalMemo],
#             account_name =  data[account_name],
#             debit =  data[debit],
#             credit =  data[credit]
#         )

#         serializer = journalEntrySeralizers(addChart, many=False)
#         return Response(serializer.data)

# this function is for journal entry list
@api_view(['GET'])
def journalEntry_list(request):
    """
    This function is for displaying list of chart of Account
    """
    journalEntry = JournalEntry.objects.all()
    serializer = journalEntrySeralizers(journalEntry, many=True)
    return Response(serializer.data)

# this function is to add journal entry
@api_view(['POST'])
def testApi(request):
    serializer = journalEntrySeralizers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# this is for deleting journal entry
@api_view(['DELETE'])
def delete_journalEntry(request, pk):
    """
    This function is to delete chart of journal entry
    """
    chartofAccount = JournalEntry.objects.get(id=pk)
    chartofAccount.delete()
    return Response('data has been removed')


# this function is fro testing class base API

class test_api(viewsets.ModelViewSet):
    queryset=JournalEntry.objects.all()
    serializer_class=journalEntrySeralizers

