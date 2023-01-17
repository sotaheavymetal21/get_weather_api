from django.http import HttpResponse


def hello_world_func(request):
    return HttpResponse("<h1>Hello World</h1>")
