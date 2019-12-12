from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.maliyetYeni, name='maliyetYeni'),
]