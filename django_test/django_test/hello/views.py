from django.shortcuts import render, HttpResponse
from . models import Tabela
# Create your views here.



def home(request):
    return render(request, "index.html", {'title' : 'index', 'content': 'bodao'})

def homehello(request):
    return HttpResponse("hellooooooooo")


def outro(request):
    return HttpResponse("outro")

def exib(request):
    items =  Tabela.objects.all()
    return render(request, "exibe_tab.html", {"title" : "Exibe tabela", "items": items})