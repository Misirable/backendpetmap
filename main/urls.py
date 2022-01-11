from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('profile/', views.profile),
    path('create/', views.create),
    path('homeless/', views.homeless),
    path('pets/', views.pets),
    path('edit/', views.edit),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
