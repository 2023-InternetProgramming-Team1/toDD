from django.urls import path
from . import views

urlpatterns = [
    path('remove/', views.remove, name="remove"),
    path('', views.PostList.as_view()),
    path('popup/', views.popup),
]

