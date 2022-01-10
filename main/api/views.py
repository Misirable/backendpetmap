from rest_framework import viewsets
from ..models import Post, PostCategory, TypeAnimal
from .serializers import PostCategorySerializer, PostSerializer, AnimalTypeSerializer

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

 	
class PostCategoryViewSet(viewsets.ModelViewSet):
	queryset = PostCategory.objects.all()
	serializer_class = PostCategorySerializer

class AnimalTypeViewSet(viewsets.ModelViewSet):
	queryset = TypeAnimal.objects.all()
	serializer_class = AnimalTypeSerializer