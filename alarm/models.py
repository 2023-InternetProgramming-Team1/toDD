from django.db import models
from django.utils import timezone
from eclass.models import Assignment, Quiz
from home.models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=Assignment) #참조키 값 생성될 때 자동 생성
def create_list_updated_assignment(sender, instance, created, **kwargs):
    if created:
        Updated.objects.create(assignment=instance)
@receiver(post_save, sender=Quiz) #참조키 값 생성될 때 자동 생성
def create_list_updated_quiz(sender, instance, created, **kwargs):
    if created:
        Updated.objects.create(quiz=instance)

class Updated(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    class Meta:
        app_label = 'alarm'

    def get_absolute_url(self):
        if self.assignment:
            return f'../../eclass/lecture/{self.assignment.activity.lecture.pk}/'
        if self.quiz:
            return f'../../eclass/lecture/{self.quiz.activity.lecture.pk}/'





@receiver(post_save, sender=Post) #참조키 값 생성될 때 자동 생성
def create_list_check_this(sender, instance, created, **kwargs):
    if created:
        CheckThis.objects.create(post=instance)

class CheckThis(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'alarm'
    def __str__(self):
        return str(self.post.title)
    def get_absolute_url(self):
        return f'../../home/check_details_{self.post.pk}/'

    def is_deadline_today(self):
        today = timezone.localtime()
        deadline = timezone.localtime(self.post.deadline)
        difference = deadline - today
        return difference.total_seconds() <= 86400 and difference.total_seconds() >= 0 and self.post.complete == False








