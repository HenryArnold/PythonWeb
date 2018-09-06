from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from poem import data, model
from poem.config import *
# Create your views here.
def getPoem(head):
    pass
    '''
    trainData=data.POEMS(trainPoems)
    xiaocai=model.MODEL(trainData)
    poem11=xiaocai.testHead(head).replace('\n','')
    poem22=xiaocai.testHead(head).replace('\n','')
    poem33=xiaocai.testHead(head).replace('\n','')
    poem1=[]
    poem2=[]
    poem3=[]
    poems=[]
    def dealPoem(poem11, poem1):
        str=''
        for i in poem11:
            str+=i
            if i=='，':
                poem1.append(str)
                str=''
            elif i=='。':
                poem1.append(str)
                str=''
        return poem1
    poem1=dealPoem(poem11, poem1)
    poem2=dealPoem(poem22, poem2)
    poem3=dealPoem(poem33, poem3)
    poems.append(poem1)
    poems.append(poem2)
    poems.append(poem3)
    return poems
    '''

def poem(request):
    context={}
    context['poems']=[]
    context['error']=''
    try:
        if 'head' in request.GET:
            head=request.GET['head']
            context['poems']=getPoem(head)
            return render(request, 'poem.html', context)
        else:
            return render(request, 'poem.html', context)
    except Exception as e:
            context['error']=e
            return render(request, 'poem.html', context)
