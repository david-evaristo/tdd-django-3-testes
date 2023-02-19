from django.shortcuts import render
from django.http import HttpResponse
from animais.models import Animal

# Create your views here.

def index(request):
    context = {'caracteristicas' : Animal.objects.all()}
    return render(request, 'index.html', context)
