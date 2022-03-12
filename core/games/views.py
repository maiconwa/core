from django.shortcuts import render
from rest_framework import viewsets
from .models import Jogos
from .serializers import JogosSerializer
# Create your views here.

class JogosViewSet(viewsets.ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer
    