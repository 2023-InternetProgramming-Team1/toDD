from django.db import models
import os
from eclass.models import Lecture, Activity, Assignment, Quiz
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/home/category/{self.slug}'

class Post(models.Model):
    # 투두 리스트 제목
    title = models.CharField(max_length=30)
    # 투두 리스트 상세 내용
    content = models.TextField()
    # 데드라인
    deadline = models.DateTimeField(auto_now=False)
    # 카테고리
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # 완료 여부
    complete = models.BooleanField(default=False)
    # 리스트 만든 날짜
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'../../home/check_details_{self.pk}/'