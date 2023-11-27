from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecture_list, name='lecture_list'),
    path('lecture/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    path('activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    path('assignment/create/<int:activity_id>/', views.assignment_creation, name='assignment_create'),
    path('quiz/create/<int:activity_id>/', views.quiz_creation, name='quiz_create'),
]