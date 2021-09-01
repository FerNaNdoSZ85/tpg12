from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from appPreguntas.models import Pregunta
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from appPreguntas.models import Pregunta #importado



#@login_required(login_url= '/') #modificado se debe mostrar home, haciendo clic en jugador debo loguearme --> login
def inicio(request):
    return render(request, "home.html")


def registro(request):
    if request.method == "POST":
        FormReg = UserCreationForm(request.POST)
        
        if FormReg.is_valid():
            FormReg.save()
            return redirect('home') #cambie login --> home, despues de loguearme voy al home
    else:
        FormReg= UserCreationForm() 
    return render(request, "registration/registro.html", {'FormReg': FormReg})


@staff_member_required
def administrador(request):
    return render(request, 'administrador/administrador_central.html')


#@login_required(login_url= '') #aca cambie '/' -->
def usuario(request):
    return render(request, 'jugador/jugador_central.html')

def agregar(request): #agregado para modificar preguntas
    return render(request, 'administrador/agregar_p.html') #agregado para modificar preguntas

def editar(request): # falta agregar id de la pregunta, que viene como parametro, (se debe ajustar la bd)
    preg = Pregunta.objects.all() # debe cambiarse .all() --> .fiter(id=id_preg)
    form = preg(instance=Pregunta)
    
    return(request, "editar",{'form':form})

def actualizar(request): # falta agregar id de la pregunta, que viene como parametro, (se debe ajustar la bd)
    preg = Pregunta.objects.all() # debe cambiarse .all() --> .get(pk=id_preg)
    
    form = preg(request.POST, instance=Pregunta)
    if form.es_valid():
        form.save()
    preg = Pregunta.objects.all()
    return(request, "editar",{'form':form})

def ListarPreguntas(request):
    preguntas=Pregunta.objects.all()
    return render(request, "listar.html", {'preguntas':preguntas})
