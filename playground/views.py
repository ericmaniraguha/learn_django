from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return HttpResponse("Welcome to the homepage!")
