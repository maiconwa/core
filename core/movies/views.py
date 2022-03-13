from django.shortcuts import render
from rest_framework import viewsets
from .models import Filmes
from .serializers import FilmesSerializer
# Create your views here.

class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
    