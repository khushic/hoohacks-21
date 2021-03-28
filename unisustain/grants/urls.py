from django.urls import path
from . import views

app_name = 'grants'

urlpatterns = [
    path('', views.get_all_grants, name='get_all'),
    path('view_grant/<int:grant_id>/', views.get_grant, name='view_grants'),
]
