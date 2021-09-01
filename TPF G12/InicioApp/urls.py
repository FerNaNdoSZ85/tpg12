from django.urls import path
from InicioApp import views
from appCuestionarios.views import Cuest
from appPreguntas.views import *
from appRespuestas.views import*
from django.contrib.auth import views as auth_Views


urlpatterns = [
    path('home/', views.inicio, name="home"),
    path('login/', auth_Views.LoginView.as_view(template_name= "registration/login.html"), name="login"), # cambio '' --> login/
    path('registro/', views.registro, name="registro"),
    path('logout/', auth_Views.LogoutView.as_view(), name = 'logout'), #cambie 'logout' --> 'home'
    path('admi/', views.administrador, name= 'admi'),
    path('user/', views.usuario, name= 'user'),
    path('agregar/', views.agregar, name= 'agregar'), #agregado modulo para agregar preguntas
    path('editar/',views.editar, name="editar"), #agregado modulo para editar preguntas
    path('listar/',views.ListarPreguntas, name="listar"), 
]
