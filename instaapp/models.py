from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from PIL import Image
import cloudinary
import datetime as dt



# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_photo = CloudinaryField('profile_photo')


    def save_profile(self):
        self.save()

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save()

    

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio)
        return update_profile

    def __str__(self):
        return self.bio


class Image(models.Model):
    gallery_image = CloudinaryField('gallery_image', null=True)
    image_name = models.CharField(max_length =30, null=True)
    image_caption = models.CharField(max_length =70, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ['pub_date']

    def save_image(self):
        '''
        Method to save our images
        '''
        self.save()

    def delete_image(self):
        '''
        Method to delete our images
        '''
        self.delete()

    @classmethod
    def update_caption(cls, self, caption):
        update_cap = cls.objects.filter(id = id).update(caption = caption)
        return update_cap

    
    def __str__(self):
        return self.image_name


class Subscribers(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
