from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello")
def ronnie(request):
    return HttpResponse("Hello, Ronnie!")
def greet(request, name):
    return HttpResponse(f'Hello {name.capitalize()}!')