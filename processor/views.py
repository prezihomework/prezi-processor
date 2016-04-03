from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

def text(request):
    return HttpResponse("Some text is here.")

def base(request):
    return render(request, 'processor/base.html')
