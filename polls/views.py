from django.http import HttpResponse


def index(request):
    response = HttpResponse("Hello, world. You're at the polls index.")
    return response
