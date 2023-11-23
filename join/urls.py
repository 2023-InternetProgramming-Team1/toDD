from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login),
    # path('<int:pk>/', views.loginout),
    path('account/', views.account),
    path('mypage/', views.mypage),
]