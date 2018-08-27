from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Counter
def counter(request):
    context['counterData']=0
    context['counterData']=Counter.objects.order_by('counterName')[:]
    response[]
    return response
