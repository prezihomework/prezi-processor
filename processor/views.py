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

        creator = Creator.objects.create(name=single_entry["creator"]["name"], profileUrl=single_entry["creator"]["profileUrl"])
        date_object = datetime.strptime(single_entry["createdAt"], '%B %d, %Y')

        #Itt van a hiba. A creator nem fogadja el a creator-t
        Prezi.objects.get_or_create(id=single_entry["id"], title=single_entry["title"], thumbnail=single_entry["thumbnail"], creator=creator,
                         pub_date=date_object)

    return HttpResponse('asd', content_type="application/json")
