
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext
import datetime
import time
from django.views.generic import TemplateView
from talleres.models import Taller
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
                cedula = usuario.estudiante.cedula
                telefono = usuario.estudiante.telefono
                programa = usuario.estudiante.contrato.programa.nombre_del_programa
                duracion = usuario.estudiante.contrato.duracion
                startdate = datetime.date.today()
                fecha = datetime.datetime.today()
                enddate = startdate + datetime.timedelta(days=6)
                talleres = Taller.objects.filter(fecha__range=[startdate, enddate]).filter(hora_inicio__gt=time.strftime("%H:%M:%S"))
                return render(request,'contenido.html',{'username':username,'fecha':fecha,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'duracion':duracion,'talleres':talleres})
            else:
                state = "Tu cuenta esta desactivada por favor acercarce a oficinas."
        else:
            state = "Usuario o contrasena incorrecta"

    return render(request,'signin.html',{'state':state}, context_instance=RequestContext(request))


def academirank (request):
    return render(request,'rank.html',context_instance=RequestContext(request))

class Busqueda_info_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_taller = request.GET['id']
        print id_taller
        info = Taller.objects.filter(id=id_taller)
        data=serializers.serialize("json", info)
        print data
        return HttpResponse(data, content_type="application/json")