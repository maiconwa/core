from turtle import mode
from django.db import models

# Create your models here.
class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autoria = models.CharField(max_length=100)
    publicacao = models.IntegerField()
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
