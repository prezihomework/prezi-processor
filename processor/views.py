from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Prezi
from .models import Creator
from datetime import datetime
import urllib
import requests

def index(request):
    return render(request, 'processor/home.html')

def contact(request):
    return render(request, 'processor/contact.html')

def test(request):
    with urllib.request.urlopen('http://localhost:8080/prezis?title=fugiat%20anim%20proident%20dolor') as response:
        html = response.read()
    return HttpResponse(str(html))

def list(request):
    queryset = Prezi.objects.all()
    queryset = serializers.serialize('json', queryset)
    return HttpResponse(queryset, content_type="application/json")

def deserialize(request):
    full_prezis = requests.get('http://localhost:8080/prezis')
    full_json = full_prezis.json()

    for i in range(len(full_json)):
        single_entry = full_json[i]
        Creator.objects.update_or_create(name=single_entry["creator"]["name"], profileUrl=single_entry["creator"]["profileUrl"])

    for i in range(len(full_json)):
        single_entry = full_json[i]
        date_object = datetime.strptime(single_entry["createdAt"], '%B %d, %Y')

        Prezi.objects.update_or_create(id=single_entry["id"], title=single_entry["title"], thumbnail=single_entry["thumbnail"], creator=Creator.objects.get(name=single_entry["creator"]["name"], profileUrl=single_entry["creator"]["profileUrl"]),
                     pub_date=date_object)

    return render(request, 'processor/deserialize.html')

def search(request, keyword=None):
    if request.POST:
        result = Prezi.objects.filter(title=request.POST.get('searchfield'))
    elif keyword != None:
        result = Prezi.objects.filter(title=keyword)
    else:
        result = Prezi.objects.all()

    return render(request, 'processor/search.html', { 'result': result })

def sortByDate(request):
    result = Prezi.objects.all().order_by('pub_date')
    return render(request, 'processor/search.html', { 'result': result })
