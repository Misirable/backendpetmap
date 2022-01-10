from django.db import models

class PostCategory(models.Model):
    title = models.CharField(max_length=70, verbose_name="Заголовок")

def __str__(self):
        return self.title

class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name="Кличка")
    type_pet = models.CharField(max_length=255, verbose_name="Вид питомца")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    location = models.CharField(max_length=50, verbose_name="Локация")
    photo = models.ImageField(verbose_name="Фото", blank=True, null = True)
    definition = models.CharField(max_length=550, verbose_name="Описание питомца")
    postcategory = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

def __str__(self):
        return self.title

class TypeAnimal(models.Model):
    pet_type = models.CharField(max_length=70, verbose_name="Вид животного")

def __str__(self):
        return self.title