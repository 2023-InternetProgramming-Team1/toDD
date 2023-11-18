from django.db import models

class Post(models.Model):
    # 투두 리스트 제목
    title = models.CharField(max_length=30)
    #투두 리스트 상세 내용
    content = models.TextField()
    # 데드라인
    deadline = models.DateField()
