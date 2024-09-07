from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Usuario
# Create your views here.
def home(request):
    return render(request,'usuarios/home.html') 
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    #exibir essas informações em uma nova página
    Usuarios = {
        'usuarios':Usuario.objects.all()
        
    }
    return HttpResponse(f"{novo_usuario.nome}{novo_usuario.email}")

