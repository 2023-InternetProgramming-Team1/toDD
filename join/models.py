from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    studentId = models.IntegerField(blank=True, null=True,unique=True)
    password = models.IntegerField(blank=True, null=True,unique=True)

    def __str__(self):
        return f"{self.username} - {self.studentId}"


class Login(models.Model):
    users = models.ManyToManyField(User, related_name='logins')
    login_path = models.CharField(max_length=100, default='join/login.html')

class Signup(models.Model):
    users = models.ManyToManyField(User, related_name='signup')
    signup_path = models.CharField(max_length=100, default='join/signup.html')
