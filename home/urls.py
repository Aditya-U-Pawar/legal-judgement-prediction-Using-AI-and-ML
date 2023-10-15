from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.Law4People, name='Law4People'),
    path("chatterbot", views.chatterbot, name='chatterbot'),
    path("logout", views.logout, name='logout'),
    path("signup", views.signup, name='signup'),
]