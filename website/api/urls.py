from django.urls import path
from . import views

urlpatterns = [
    path('salam/',views.print, name='salam'),
    path('func/',views.getData),
]