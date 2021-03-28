from django.urls import path
from . import views

app_name = 'research-forum'

urlpatterns = [
    path('', views.get_all_questions, name='questions'),
    path('view_questions/<int:question_id>/', views.get_question, name='view_questions'),
    path('new_question/', views.create_question, name='new_forum_question'),
    path('new_comment/<int:question_id>/', views.create_comment, name='new_forum_comment'),
]
