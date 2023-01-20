from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.

# BookListに合わせて継承していく
class TopView(ListView):
    template_name = "list.html"
    # どのデータを使うのかを明示する
    model = Book
