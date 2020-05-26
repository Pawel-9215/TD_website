from django.contrib import admin
from django.urls import path
from AppTwo import views

urlpatterns = [
    path("", views.index, name='index'),
    path("help/", views.help, name='help'),
    path("gallery/", views.gallery, name='gallery'),
    path("users/", views.help, name='users'),
]