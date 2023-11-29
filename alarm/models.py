from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    category= models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/alarm/{self.pk}'




