from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'processor/home.html')

def contact(request):
    return render(request, 'processor/contact.html')


