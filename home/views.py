from django.http import HttpResponse

def home(request):
    response = HttpResponse("Hello, world. You're at the homepage now.")
    return response
