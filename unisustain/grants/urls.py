from django.urls import path

from . import views

urlpatterns = [
    path('grants/', views.get_all_grants, name='get_all'),
    path('view_grant/', views.get_grant, name='get_grant'),
    #path('view_grant/<int:grant_id>/', views.get_grant, name='get_grant'),
]
