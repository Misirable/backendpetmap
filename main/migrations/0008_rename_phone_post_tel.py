# Generated by Django 3.2.4 on 2022-01-10 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220111_0510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='phone',
            new_name='tel',
        ),
    ]