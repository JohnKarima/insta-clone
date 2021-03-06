# Generated by Django 3.1.2 on 2020-10-17 19:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaapp', '0004_auto_20201017_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='gallery_image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
