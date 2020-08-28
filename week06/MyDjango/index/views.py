from django.shortcuts import render
from django.http import HttpResponse
from . models import Film
# Create your views here.
def index(request):
    return HttpResponse('第六周作业')

def films(request):
    # n = Film.objects.all()
    n = Film.objects.filter(stars__gt=3)

    return render(request, 'index.html', locals())