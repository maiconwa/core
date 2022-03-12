from rest_framework import serializers
from .models import Jogos

# Serializers define the API representation.
class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogos
        fields = ['id', 'titulo', 'desenvolvedora', 'distribuidora', 'genero', 'plataformas', 'publicacao']