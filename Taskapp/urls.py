from django.urls import path,include
from Taskapp import views
from Taskapp.views import home
from .views import *




urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name= 'hello'),
   
    
    
]