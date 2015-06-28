from django.shortcuts import render
from django.contrib import auth
from forms import Contrato
# Create your views here.
def contrato(request):
    if request.method == 'POST':
        form = Contrato(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        return HttpResponseRedirect('usuario/gracias/')
    else:
        form = Contrato()
    return render(request,'usuario/registro.html',{'form':form})
