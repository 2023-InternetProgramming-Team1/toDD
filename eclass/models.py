from django.db import models
from django.contrib.auth.models import User

class Lecture(models.Model):
    name = models.CharField(max_length=100)

class Activity(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    week = models.IntegerField()
    title = models.CharField(max_length=50)

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    content = models.TextField()
    activity = models.OneToOneField('Activity', on_delete=models.CASCADE)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    questions = models.TextField()
    activity = models.OneToOneField('Activity', on_delete=models.CASCADE)