from django.contrib import admin
from .models import Lecture, Activity, Assignment, Quiz

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Activity)
admin.site.register(Assignment)
admin.site.register(Quiz)