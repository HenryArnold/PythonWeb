from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Logs
def logs(request):
    context = {}
    context['logs']=[]
    context['logs']=Logs.objects.order_by('-data')[:]
    return render(request, 'logs.html', context)
