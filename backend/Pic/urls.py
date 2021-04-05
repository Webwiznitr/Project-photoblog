from django.contrib import admin
from django.urls import path ,include
from Pic import views

urlpatterns = [
     path("",views.index,name ='home')
]
