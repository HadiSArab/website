from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  . import hadi

@api_view(['GET'])
def print(request):
    hadi = "salam"
    return Response(hadi)

@api_view(['GET'])
def getData(request):
    res = hadi.funcs.sam()
    return Response(res)