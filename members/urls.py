from django.contrib import admin
from django.urls import path
from .views import UserRegisterView
#from . import views


urlpatterns = [ 
    path('regiser/', UserRegisterView.as_view(), name='register'),
    
     
]   