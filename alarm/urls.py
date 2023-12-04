from django.urls import path
from . import views

urlpatterns = [
    path('', views.alarm),
    path('<int:pk>/remove_check_this/', views.remove_check_this),
    path('<int:pk>/remove_assignment/', views.remove_assignment),
    path('<int:pk>/remove_quiz/', views.remove_quiz),
]

