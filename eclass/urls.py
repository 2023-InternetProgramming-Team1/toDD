from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecture_list, name='lecture_list'),
    path('lecture/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    path('activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    path('activity/<int:activity_id>/quiz/create/', views.quiz_create, name='quiz_create'),
    path('activity/<int:activity_id>/assignment/create/', views.assignment_create, name='assignment_create'),
]