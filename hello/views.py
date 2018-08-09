from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

def GetId(url):
    list0=[]
    str0=''
    url+='/'
    for i in url:
        str0+=i
        if i=='/':
            list0.append(str0.strip('/'))
            str0=''

    ids = list0[-1]
    name = list0[-2]
    return (ids, name)


'''
def download(url):
    id=GetId(url)
    crx='https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D'+id+'%26installsource%3Dondemand%26uc'
    return HttpResponse('Hello')

    import urllib.request
    try:
        crx=urllib.request.urlopen(crx).read()
        return HttpResponse(crx)
    except:
        context['error']='the link is weak'
        return (context['error'])

        '''
# Create your views here.
def index(request):
    context = {}
    context['error'] =''
    if 'url' in request.GET:
        url = request.GET['url']
        ids, name=GetId(url)
        crx='https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D'+ids+'%26installsource%3Dondemand%26uc'
        return HttpResponse(crx)
        import urllib.request
        try:
            crx=urllib.request.urlopen(crx).read()
            return HttpResponse(crx)
        except:
            context['error']='the link is weak'

    return render(request, 'index.html', context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
