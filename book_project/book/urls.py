from django.urls import path

from .views import BookList, BookListAPI, WeatherDetailView

urlpatterns = [
    path("list/", BookList.as_view()),
    path("api/", BookListAPI.as_view()),
    path("detail/<int:pk>/", WeatherDetailView.as_view()),
]
