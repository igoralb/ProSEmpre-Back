from django.shortcuts import render
from .models import Equipe, LegendaBanner, NossasFerramentas, Artigos, PlataformaVideos, MateriaisApoio, PlataformaJogos, Contato, Informacoes

def index(request):
    equipe = Equipe.objects.all()
    legenda_banner = LegendaBanner.objects.first()
    nossas_ferramentas = NossasFerramentas.objects.all()
    artigos = Artigos.objects.all()
    plataforma_videos = PlataformaVideos.objects.first()
    materiais_apoio = MateriaisApoio.objects.all()
    plataforma_jogos = PlataformaJogos.objects.first()
    contato = Contato.objects.first()
    informacoes = Informacoes.objects.all()
    
    context = {
        'equipe':equipe,
        'legenda_banner': legenda_banner,
        'nossas_ferramentas': nossas_ferramentas,
        'artigos': artigos,
        'plataforma_videos': plataforma_videos,
        'materiais_apoio': materiais_apoio,
        'plataforma_jogos': plataforma_jogos,
        'contato':contato,
        'informacoes':informacoes,
    }
    
    return render(request, 'index.html', context)

def videos_view(request):
    return render(request, 'videos.html')

def forum_view(request):
    return render(request, 'forum.html')

def pais_profs_view(request):
    return render(request, 'pais_profs.html')
