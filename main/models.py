from django.db import models


class PostCategory(models.Model):
    title = models.CharField(max_length=70, verbose_name="Название категории")

    def __str__(self):
        return f"{self.title}"


class TypeAnimal(models.Model):
    pet_type = models.CharField(max_length=70, verbose_name="Вид животного")

    def __str__(self):
        return f"{self.pet_type}"


class Post(models.Model):
    description = models.CharField(max_length=510, verbose_name="Описание питомца")
    type_pet = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE, verbose_name="Вид питомца")
    tel = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name='email')
    name = models.CharField(max_length=125, verbose_name='Имя')
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")
    photo = models.ImageField(verbose_name="Фото", blank=True, null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return f"{self.id}"
