from django.db import models

# Create your models here.
class Filmes(models.Model):
    titulo = models.CharField(max_length=100)
    direcao = models.CharField(max_length=100)
    lancamento = models.IntegerField()
    
    def __str__(self):
        return self.titulo