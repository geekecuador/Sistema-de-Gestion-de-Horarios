from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout

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
                return render(request,'account.html',{'username':username})
            else:
                state = "Tu cuenta esta desactivada por favor acercarce a oficinas."
        else:
            state = "Usuario o contrasena incorrecta"

    return render(request,'signin.html',{'state':state})
