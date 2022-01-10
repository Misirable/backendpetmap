from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('profile', views.profile),
    path('create', views.create),
    path('homeless', views.homeless),
    path('pets', views.pets),
    path('edit', views.edit),
]
