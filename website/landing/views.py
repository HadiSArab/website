from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def landing(request):
    return HttpResponse("Hello world!")

def photos(request):
    return(HttpResponse("this is photos of you"))

def camera(request):
  template = loader.get_template('camera.html')
  return HttpResponse(template.render())