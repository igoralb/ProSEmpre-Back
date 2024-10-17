from django.shortcuts import render
from .models import Equipe, LegendaBanner, NossasFerramentas, Artigos, PlataformaVideos, MateriaisApoio, PlataformaJogos

def index(request):
    equipe = Equipe.objects.all()
    legenda_banner = LegendaBanner.objects.first()
    nossas_ferramentas = NossasFerramentas.objects.all()
    artigos = Artigos.objects.all()
    plataforma_videos = PlataformaVideos.objects.first()
    materiais_apoio = MateriaisApoio.objects.all()
    plataforma_jogos = PlataformaJogos.objects.first()
    
    context = {
        'equipe':equipe,
        'legenda_banner': legenda_banner,
        'nossas_ferramentas': nossas_ferramentas,
        'artigos': artigos,
        'plataforma_videos': plataforma_videos,
        'materiais_apoio': materiais_apoio,
        'plataforma_jogos': plataforma_jogos,
    }
    
    return render(request, 'index.html', context)

def home_view(request):
    return render(request, 'home.html')

def videos_view(request):
    return render(request, 'videos.html')

def forum_view(request):
    return render(request, 'forum.html')

def pais_profs_view(request):
    return render(request, 'pais_profs.html')
