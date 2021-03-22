# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.blogHome, name="blogHome"),
   path('postcomment/',views.PostComment,name='postcomment'), #this must be above the '<str:slug>/' url
   path('<str:slug>/',views.blogPost,name='blogPost'),
]
