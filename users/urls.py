from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('' , Home , name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
    path('logout/' , Logout , name="logout"),
    path('posts/',posts, name="posts"),
    path("addpost/",addpost, name="addpost"),
    
 
]
