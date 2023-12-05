from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    studentId = models.IntegerField(blank=True, null=True,unique=True)
    number = models.IntegerField(blank=True, null=True,unique=True)

    def __str__(self):
        return f"{self.username} - {self.studentId}"


class login(models.Model):
    users = models.ManyToManyField(User, related_name='login')
    login='join/login.html'

class account(models.Model):
    users = models.ManyToManyField(User, related_name='account')
    account='join/account.html'



