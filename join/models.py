from django.contrib.auth.models import AbstractUser
from eclass.models import Lecture
from django.db import models


# Create your models here.

class User(AbstractUser):
    studentId = models.IntegerField(blank=True, null=True, unique=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'studentId'  # 이 부분을 추가하여 studentId를 로그인에 사용

    def __str__(self):
        return f"{self.username} - {self.studentId}"