from rest_framework import serializers
from .models import Livros

# Serializers define the API representation.
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id', 'nome','autoria', 'publicacao', 'tipo']