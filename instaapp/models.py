from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_photo = CloudinaryField('profile_photo')


    def __str__(self):
        return self.bio
