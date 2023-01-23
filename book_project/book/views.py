from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView

from .models import Book, Weather
from .serializers import BookSerializer

# Create your views here.

# BookListに合わせて継承していく
class BookList(ListView):
    template_name = "list.html"
    model = Book


class BookListAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []


class WeatherDetailView(DetailView):
    model = Weather
    template_name = "detail.html"
