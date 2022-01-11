from django.contrib import admin
from .models import Post, PostCategory, TypeAnimal

admin.site.register(Post)
admin.site.register(TypeAnimal)
admin.site.register(PostCategory)
# Register your models here.
