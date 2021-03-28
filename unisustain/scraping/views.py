from django.shortcuts import render
from django.views import generic
from .models import Scraping
# Create your views here.
class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'

    def get_querySet(self):
        return Scraping.objects.all()
