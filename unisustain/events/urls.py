from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.get_all_events, name='events'),
    path('view_events/<int:event_id>/', views.get_event, name='view_events'),
    path('new_event/', views.create_event, name='new_event'),
    path('filter_events/', views.filter_events, name='filter_events'),
]
