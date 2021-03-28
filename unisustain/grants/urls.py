from django.urls import path
from . import views

app_name = 'grants'

urlpatterns = [
    path('', views.get_all_grants, name='grants'),
    path('view_grants/<int:grant_id>/', views.get_grant, name='view_grants'),
    path('new_grant/', views.create_grant, name='new_grant'),
]
