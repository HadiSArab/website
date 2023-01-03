from django.urls import path
from . import views

urlpatterns = [
    path('',views.empty),
    path('serializing/',views.serializing, name='salam'),
    path('scores/',views.class_members, name = 'members_score'),
    path('additem/',views.additems),
]