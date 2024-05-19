# models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    about = models.TextField()
    contact_message = models.TextField(blank=True)
    education = models.TextField(max_length=50)
    profile_image = models.ImageField(upload_to='images/')
    email = models.EmailField()
    location= models.CharField(max_length=300, null=True)
    language = models.CharField(max_length=300, null=True)
    phone_number = models.CharField(max_length=15)
    work_status = models.CharField(max_length=20)
    facebook = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    skype = models.URLField(blank=True)


    def __str__(self):
        return self.name
    
class WhatIDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title