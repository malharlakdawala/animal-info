from django.shortcuts import render
from django.http import HttpResponse
from info.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def family(request,id):
    animal= Animal.objects.get(id=id)
    return render(request, 'family.html', {'animal': animal})

def animal(request,id):
    pass

def animals(request):
    animals= Animal.objects.all()
    return render(request, 'animals.html', {'animals': animals})