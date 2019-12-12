from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.sureYeni, name='sureYeni'),
]