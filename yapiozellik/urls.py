from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.yapiOzellikYeni, name='yapiOzellikYeni'),
]