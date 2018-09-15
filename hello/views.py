from django.shortcuts import render
from django.http import HttpResponse

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
    str1=''
    for i in ids:
        if i=='?':
            break
        str1+=i
    ids=str1
    name = list0[-2]
    return (ids, name)
def Extension(url):
    ids,the_file_name=GetId(url)
    the_file_name+=".crx"
    crx='https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D'+ids+'%26installsource%3Dondemand%26uc'
    return the_file_name, crx

def Youtube(url):
    import os
    command="youtube-dl "+url
    mp3=os.system(command)
    the_file_name=mp3.basename()
    return the_file_name, mp3
# Create your views here.
def index(request):
    from django.http import StreamingHttpResponse
    chunk_size=512
    context = {}
    context['error'] =''
    '''
    try:
        if 'url' in request.GET:
            url = request.GET['url']
            ids, the_file_name=GetId(url)
            the_file_name+=".crx"
            crx='https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D'+ids+'%26installsource%3Dondemand%26uc'
            import urllib.request
            crx=urllib.request.urlopen(crx).read()
            response =  HttpResponse(crx, content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
            return response
            #return HttpResponse(crx)
    '''
    try:
        if 'url' in request.GET:
            url=request.GET['url']
            if "webstore" in url:
                the_file_name,file=Extension()
            if "youtube" in url:
                the_file_name,file=Youtube()
            import urllib.request
            file=file.read()
            response =  HttpResponse(file, content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
            return response
    except:
        context['error']='The link is weak'
    return render(request, 'index.html', context)

def help(request):
    return render(request, 'help.html')

def google(request):
    return render(request, 'google740430dd129e0ed2.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})
