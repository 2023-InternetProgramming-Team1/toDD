from django.urls import path
from . import views

urlpatterns = [
    path('add_list/', views.PostCreate.as_view()),
    path('check_details_<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('category/<str:slug>/', views.category_page),
]