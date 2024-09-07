from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=300)
    telefone = models.IntegerField()
    senha = models.CharField(max_length=10)
    data_nascimento = models.DateField(null=True)
   
    
