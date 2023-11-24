from django.urls import path
from . import views

urlpatterns = [
    path('add_list/', views.PostCreate.as_view()),
    path('check_details_<int:pk>/', views.PostDetail.as_view()),

    # 메인
    path('', views.PostList.as_view()),
    # 카테고리 별
    path('category/<str:slug>/', views.category_page),
    # 컴플리트
    path('todo_complete/<int:pk>/', views.todo_complete),
    path('todo_incomplete/<int:pk>/', views.todo_incomplete),
]