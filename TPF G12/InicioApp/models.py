from django.db import models

# Create your models here.
from django.contrib.auth.models import User # AGREGADO
from django.contrib.auth.forms import UserCreationForm # AGREGADO
from django.views.generic import CreateView # AGREGADO
from django.urls import reverse # AGREGADO

class Usuarios(CreateView): # modelo modificado... se tiene que hacer de nuevo la migracion :S
    model = User
    template_name = "registration/login.html"
    form_class = UserCreationForm
    success_url = reverse('home')    
    """"
    dni= models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=25,null=False, blank=True)
    correo = models.CharField(max_length=25,null=False, blank=True)
    contrasenia = models.CharField(max_length=16, null=False, blank=True)
    """
    class Meta:
        db_table = 'usuarios'
    
    #def __str__(self):
    #    txt ="{0} / {1} / {2}"
    #    return txt.format(self.nombre, self.dni, self.correo)