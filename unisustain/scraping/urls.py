from django.urls import path
from . import views

app_name = 'scraping'

urlpatterns = [
    path('', views.get_querySet(), name='scraping'),
]