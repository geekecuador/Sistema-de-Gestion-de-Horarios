from django.shortcuts import render
from django.contrib import auth
from forms import Contrato
# Create your views here.

def landing(request):
    return render(request,'index.html')