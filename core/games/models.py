from django.db import models

# Create your models here.
class Jogos(models.Model):
    titulo = models.CharField(max_length=100)
    desenvolvedora = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataformas = models.CharField(max_length=100)
    publicacao = models.IntegerField()
    
    def __str__(self):
        return self.titulo
