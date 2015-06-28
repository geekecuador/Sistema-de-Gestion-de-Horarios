__author__ = 'david'
from django.contrib import admin
from models import Contrato,Beneficiario,Ciudad,Sede,Pagos

admin.site.register(Contrato)
admin.site.register(Beneficiario)
admin.site.register(Ciudad)
admin.site.register(Sede)
admin.site.register(Pagos)