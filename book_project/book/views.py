from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Weather

# Create your views here.

# BookListに合わせて継承していく
class TopView(ListView):
    model = Weather
    template_name = "top.html"


class WeatherDetailView(DetailView):
    model = Weather
    template_name = "detail.html"
