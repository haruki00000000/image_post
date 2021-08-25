# Generated by Django 2.2.17 on 2021-08-25 07:47

import django.core.validators
from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='file_name',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=post.models.image_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]