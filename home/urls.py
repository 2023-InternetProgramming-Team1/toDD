from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('delete_<int:pk>/', views.postDelete, name='postDelete'),
    path('edit_list_<int:pk>/', views.postEdit, name='postEdit'),
    path('add_list/', views.postCreate, name='postCreate'),
    path('check_details_<int:pk>/', views.PostDetail.as_view()),

    # 메인
    path('', views.PostList.as_view(), name='post_list'),
    # 카테고리 별
    path('category/<str:slug>/', views.category_page, name='category'),
    # 컴플리트(메인)
    path('todo_check/<int:pk>/', views.todo_check, name='todo_check'),
    # 컴플리트(카테고리)
    path('category/<str:slug>/todo_check_category/<int:pk>/', views.todo_check_category, name='todo_check_category'),
    path('category/no_category/<int:pk>/', views.todo_check_no_category, name='todo_check_no_category'),
    # 날짜 넘기기
    path('change_date_next/', views.PostList.as_view(), name='change_date_next'),

    path('todo_check2/<int:pk>/', views.todo_check2, name='todo_check2'),

    path('my/', views.my, name='my'),
    ]