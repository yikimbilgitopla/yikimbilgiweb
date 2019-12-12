from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.geridonusumyeni, name='geridonusumyeni'),
]