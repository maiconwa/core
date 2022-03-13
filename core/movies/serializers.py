from dataclasses import fields
from rest_framework import serializers
from .models import Filmes

# Serializers define the API representation.
class FilmesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filmes
        fields = ['id', 'titulo', 'direcao', 'lancamento']