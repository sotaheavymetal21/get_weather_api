from django.http import HttpResponse
from django.views.generic import TemplateView


def hello_world_func(request):
    return HttpResponse("<h1>Hello World</h1>")


class HelloWorldClass(TemplateView):
    template_name = "hello.html"
