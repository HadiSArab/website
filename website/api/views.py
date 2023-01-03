from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  api.models import item
from .serializers import ItemSerializer

@api_view(['GET'])
def serializing(request):
    items = item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def class_members(request):
    dictionary = {"ali" : "20" , "hassan" : "18" , "mamad" : "15"}
    return Response(f"Nomarat Kelas Be sharhe Zir Mibashad : {dictionary}")

def empty(request):
    return HttpResponse("this is empty Request")

@api_view(['POST'])
def additems(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()