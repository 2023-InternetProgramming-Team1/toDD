from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    questions = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)