import urllib
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.files import File
from django.core.files.base import ContentFile
from PIL import Image
import PIL
import os
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from socialmediaapp import settings


# Create your models here.
fs = FileSystemStorage(location='/media/photos')

class Item(models.Model):
    image_file = models.ImageField(upload_to='images/')
    image_url = models.URLField()

    def cache(self):
        """Store image locally if we have a URL"""

        if self.image_url and not self.image_file:
            result = urllib.request.urlretrieve(self.image_url)
            #     print(result, "Sumit\n")
            self.image_file.save(
                os.path.basename("Sumit_Image_"+".jpg"),
                File(open(result[0], "rb"))
            )
            self.save()

    def __str__(self):
        return self.image_url, self.image_file

class MyPosts(models.Model):
    post_url = models.URLField()
    status_type = models.CharField(max_length=100, default='SOME STRING')
    status_source = models.CharField(max_length=100, default='SOME STRING')
    caption = models.CharField(max_length=100, default='SOME STRING')
    post_time = models.DateTimeField(auto_now=False)

class MyInformation(models.Model):
    user_first_name = models.CharField(max_length=100, default='SOME STRING')
    user_last_name = models.CharField(max_length=100, default='SOME STRING')
    birthday = models.CharField(max_length=100, default='SOME STRING')
    user_email = models.CharField(max_length=100, default='SOME STRING')
    present_location= models.CharField(max_length=100, default='SOME STRING')
    user_hometown = models.CharField(max_length=100, default='SOME STRING')
    user_first_language = models.CharField(max_length=100, default='SOME STRING')
    user_second_language = models.CharField(max_length=100, default='SOME STRING')
    number_of_friends = models.IntegerField(null=True)
    number_of_likes = models.IntegerField(null=True)
class MyLikes(models.Model):
    like_link = models.URLField(null=True)
    like_subject = models.CharField(max_length=100, default='SOME STRING')
