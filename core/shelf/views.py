from django.shortcuts import render
from rest_framework import viewsets
from .models import Livros
from .serializers import LivrosSerializer
# Create your views here.

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    