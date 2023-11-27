from django.urls import path
from . import views

urlpatterns = [
    # 시작 페이지
    path('', views.landing),
    # 어바웃어스 페이지
    path('about_us/', views.about_us),
]