from rest_framework import serializers

from ..models import Post, PostCategory, TypeAnimal
from django.contrib.auth.models import User


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAnimal  # Таблица
        fields = '__all__'  # Поля таблицы


class PostSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer()
    type_pet = AnimalTypeSerializer()

    class Meta:
        model = Post  # Таблица
        fields = '__all__'  # Поля таблицы


class PostRetriveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post  # Таблица
        fields = '__all__'  # Поля таблицы
