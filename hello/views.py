from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
#    return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def GetId(url):
    id=''
    for i in url:
        if i=='/':
            id=''
        else:
            id=id+i
    return id

def download(url):
    id=GetId(url)
    crx='https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D'+id+'%26installsource%3Dondemand%26uc'

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
