from django.urls import path
from . import views

urlpatterns = [
    # 시작 페이지
    path('', views.landing),
]