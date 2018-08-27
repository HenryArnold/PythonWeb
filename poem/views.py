from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getPoem(head):
    poem1=[]
    poem2=[]
    poem3=[]
    poems=[]
    poem1.append('小家未得美声深，')
    poem1.append('菜土裁瑶改浅深。')
    poem1.append('威自往来全寸地，')
    poem1.append('武平遗迹莫孤舟。')
    poem2.append('小家未得美声深，')
    poem2.append('菜土裁瑶改浅深。')
    poem2.append('威自往来全寸地，')
    poem2.append('武平遗迹莫孤舟。')
    poem3.append('小家未得美声深，')
    poem3.append('菜土裁瑶改浅深。')
    poem3.append('威自往来全寸地，')
    poem3.append('武平遗迹莫孤舟。')
    poems.append(poem1)
    poems.append(poem2)
    poems.append(poem3)
    return poems
def poem(request):
    context={}
    context['poems']=[]
    try:
        if 'head' in request.GET:
            head=request.GET['head']
            context['poems']=getPoem(head)
            return render(request, 'poem.html', context)
        else:
            return render(request, 'poem.html', context)
    except:
            context['error']='error'
            return render(request, 'poem.html', context)
