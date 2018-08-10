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
'''
#from django.http import StreamingHttpResponse
def big_file_download(request):
    from django.http import StreamingHttpResponse
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
            the_file_name = "big_file.pdf"
            response = StreamingHttpResponse(file_iterator(the_file_name))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
            return response

def file_download(request):

'''
'''
# Create your views here.
def index(request):
    from django.http import StreamingHttpResponse
    chunk_size=512
    context = {}
    context['error'] =''
    if 'url' in request.GET:
        url = request.GET['url']
        ids, the_file_name=GetId(url)
        crx='https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D'+ids+'%26installsource%3Dondemand%26uc'

        def file_iterator(file_name, chunk_size=512):
            with open(file_name) as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
                the_file_name = "big_file.pdf"
                response = StreamingHttpResponse(file_iterator(the_file_name))
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
                return response

        import urllib.request
        try:
            crx=urllib.request.urlopen(crx)


            while True:
                c = crx.read(chunk_size)
                if c:
                    yield c
                else:
                    return
            response = StreamingHttpResponse(file_iterator(the_file_name))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
            return response


            #return HttpResponse(crx)
        except:
            context['error']='the link is weak'

    return render(request, 'index.html', context)

'''
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
