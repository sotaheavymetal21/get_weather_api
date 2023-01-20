from django.urls import path
from .views import TopView

urlpatterns = [
    path("list/", TopView.as_view()),
]
