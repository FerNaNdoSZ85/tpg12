from InicioApp.models import Usuarios
from django.contrib import admin
from appCuestionarios.models import Cuest
from appPreguntas.models import Pregunta,Respuesta
from appRespuestas.models import Result
# Register your models here.

#admin.site.register(Usuarios) # lo saque por que me dada un error
admin.site.register(Cuest)