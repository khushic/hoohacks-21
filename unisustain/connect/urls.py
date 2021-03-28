from django.urls import path
from . import views

app_name = 'student-connect'

urlpatterns = [
    path('', views.get_all_posts, name='posts'),
    path('view_posts/<int:post_id>/', views.get_post, name='view_posts'),
    path('new_post/', views.create_post, name='new_post'),
    path('new_comment/<int:post_id>/', views.create_comment, name='new_connect_comment'),
    path('filter_posts/', views.filter_posts, name='filter_posts'),
]
