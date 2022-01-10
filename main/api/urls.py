from django.urls import path, include
from rest_framework import  routers
from .views import PostViewSet, PostCategoryViewSet, AnimalTypeViewSet
router = routers.SimpleRouter()
router.register('post', PostViewSet, basename='post')
router.register('category', PostCategoryViewSet, basename='category')
router.register('type', AnimalTypeViewSet, basename='type')


urlpatterns = [
    
]
urlpatterns += router.urls