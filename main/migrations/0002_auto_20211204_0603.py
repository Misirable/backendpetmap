# Generated by Django 3.2.4 on 2021-12-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='PostCategory',
            new_name='postcategory',
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]