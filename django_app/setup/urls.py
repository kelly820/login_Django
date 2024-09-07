
from django.contrib import admin
from django.urls import path
from  todos.views import usuarios
#importar a função da views (app)
from todos.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    #rota, views responsavel e nome de referencia
    path('', home, name='home'),
    #usuarios.cpm/usuarios
    path('usuarios/',usuarios, name='listagem_usuarios')
]
