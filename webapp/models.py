from django.db import models
from datetime import datetime
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.urls import reverse
# Create your models here.
class magazine(models.Model):
    heading=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='media/magazine/')
    likes=models.ManyToManyField(User,related_name='likes',blank=True)   
    description=models.TextField() 
    createddate=models.DateTimeField(default=datetime.now,blank=True)
    def li(self):
        return self.likes.count()
    def __str__(self):
        return self.name
class checkavl(models.Model):
    fullname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)   
    need=models.CharField(max_length=255) 
    details=models.CharField(max_length=255) 
    date=models.CharField(max_length=255) 
    accepted=models.BooleanField(default=False)
    rejected=models.BooleanField(default=False)
    photo=models.ImageField(upload_to='media/post/')
    def __str__(self):
        return self.email


class comment(models.Model):
    post=models.ForeignKey(magazine,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=160)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.user.username
        

   
        
