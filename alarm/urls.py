from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('popup/', views.popup),
    path('<int:pk>/remove/', views.remove_post),
]

