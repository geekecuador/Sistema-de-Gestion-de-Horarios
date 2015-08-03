from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext
from masterkey.models import Estudiante

def login_user(request):
    state = "Por favor ingrese a continuacion"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Conectado con exito"
                usuario = User.objects.get(username=username)
                fotourl = usuario.estudiante.foto.url
                return render(request,'contenido.html',{'username':username,'fotourl':fotourl})
            else:
                state = "Tu cuenta esta desactivada por favor acercarce a oficinas."
        else:
            state = "Usuario o contrasena incorrecta"

    return render(request,'signin.html',{'state':state}, context_instance=RequestContext(request))


def academirank (request):
    return render(request,'rank.html',context_instance=RequestContext(request))

