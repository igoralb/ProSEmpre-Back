from django.db import models

#Modelo para a equipe
class Equipe(models.Model):
    nome = models.CharField(verbose_name='Nome da pessoa', max_length=50)
    profissao = models.CharField(verbose_name='Profissão', max_length=100)
    registro_profissional = models.CharField(verbose_name='Registro Profissional', max_length=20, blank=True)
    foto = models.ImageField(upload_to='equipe_fotos/', verbose_name='Foto da pessoa')
from django.db import models

# Modelo para os textos da legenda do banner
class LegendaBanner(models.Model):
    texto = models.TextField(verbose_name="Texto da legenda do banner")

    def __str__(self):
        return "Texto da legenda do banner"

# Modelo para os textos das nossas ferramentas
class NossasFerramentas(models.Model):
    ferramenta = models.CharField(max_length=50, verbose_name="Ferramenta")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return self.ferramenta

# Modelo para os artigos
class Artigos(models.Model):
    imagem = models.ImageField(upload_to='artigos_fotos/', verbose_name='Foto do artigo')
    titulo = models.CharField(max_length=100, verbose_name="Título do artigo")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return self.titulo

# Modelo para os vídeos
class PlataformaVideos(models.Model):
    texto_principal = models.CharField(max_length=255, verbose_name="Texto principal")
    subtitulo = models.CharField(max_length=255, verbose_name="Subtítulo")

    def __str__(self):
        return "Plataforma de vídeos"

# Modelo para os materiais de apoio
class MateriaisApoio(models.Model):
    nome_material = models.CharField(max_length=100, verbose_name="Nome do material")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return self.nome_material

# Modelo para a plataforma de jogos digitais
class PlataformaJogos(models.Model):
    texto_principal = models.CharField(max_length=255, verbose_name="Texto principal")
    subtitulo = models.CharField(max_length=255, verbose_name="Subtítulo")

    def __str__(self):
        return "Plataforma de jogos digitais"

    def __str__(self):
        return self.nome
