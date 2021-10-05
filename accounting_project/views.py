from rest_framework import serializers, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import note
from .serializers import noteSeralizers

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

@api_view(['GET'])
def getNotes(request):
    notes = note.objects.all()
    serializer = noteSeralizers(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
    notes = note.objects.get(id=pk)
    serializer = noteSeralizers(notes, many=False)
    return Response(serializer.data)

# this is to update data from note model
@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    notes = note.objects.get(id=pk)
    serializer = noteSeralizers(instance=notes,data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    notes = note.objects.get(id=pk)
    notes.delete()
    return Response('data has been removed')

@api_view(['POST'])
def post_data(request):
    # data = request.data
    # notes = note.objects.create(
    #     body=data['body']
    # )
    # serializer = noteSeralizers(notes, many=False)
    # return Response(serializer.data)

    serializer = noteSeralizers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    notes = note.objects.get(id=pk)
    serializers = noteSeralizers(instance=notes, data=data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data) 


@api_view(['DELETE'])
def deleteNote(request, pk):
    notes = note.objects.get(id=pk)
    notes.delete()
    return Response('data was deleted')

@api_view(['GET'])
def searchNote(request,pk):
    # myDate = pk2
    # formatedDate = myDate.strftime("%Y-%m-%d")

    data = request.data
    notes = note.objects.filter(body__contains=pk)
    # notes = notes.filter(created__lte=formatedDate)
    
    serializer = noteSeralizers(notes, many=True)
    return Response(serializer.data)
    

class NoteList(generics.ListAPIView):
    serializer_class = noteSeralizers
   

    def get_queryset(self):
        """
        This view should return a list of all the notes
        for the currently body.
        """
       
        notes = self.kwargs['pk']
       
        return note.objects.filter(body=notes)


class NoteListDetails(generics.ListAPIView):
    queryset = note.objects.all()
    serializer_class = noteSeralizers
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['$body']
