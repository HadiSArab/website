from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('photos/',views.photos, name='photos'),
    path('camera/',views.camera, name='camera'),
]