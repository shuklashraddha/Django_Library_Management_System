import uuid
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Bookname = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Describe = models.CharField(max_length=200)
    
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.Bookname

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        
        return url

class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)