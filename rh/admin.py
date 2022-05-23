from django.contrib import admin

from .models import *


admin.site.register(Departamento)
admin.site.register(Colaborador)
admin.site.register(Cargo)
admin.site.register(FolhaPagamento)
admin.site.register(Ponto)
admin.site.register(Empresa)
admin.site.register(NotaFiscal)
admin.site.register(ItemNotaFiscal)