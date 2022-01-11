from rest_framework import viewsets
from ..models import Post, PostCategory, TypeAnimal
from .serializers import PostCategorySerializer, PostSerializer, AnimalTypeSerializer, PostRetriveSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostRetriveSerializer
    action_to_serializer = {
        "list": PostSerializer,
        "retrive": PostRetriveSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(self.action, self.serializer_class)


class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = TypeAnimal.objects.all()
    serializer_class = AnimalTypeSerializer
