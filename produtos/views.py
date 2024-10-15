from django.shortcuts import render
from .models import Equipe

def index(request):
    return render(request, 'index.html', {'equipe': Equipe.objects.all()})
