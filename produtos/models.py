from django.db import models

# Model para a equipe
class Equipe(models.Model):
    nome = models.CharField(verbose_name='Nome da pessoa', max_length=50)
    profissao = models.CharField(verbose_name='Profissão', max_length=100)
    registro_profissional = models.CharField(verbose_name='Registro Profissional', max_length=20, blank=True)
    imagem = models.ImageField(upload_to='equipe_fotos/', verbose_name='Foto da pessoa')

    def __str__(self):
        return self.nome


# Model da legenda do banner
class LegendaBanner(models.Model):
    texto = models.TextField(verbose_name="Texto da legenda do banner")

    def __str__(self):
        return "Texto da legenda do banner"

# Model das nossas ferramentas
class NossasFerramentas(models.Model):
    normal = models.CharField(max_length=50, verbose_name="Texto ferramenta normal",default="")
    destaque = models.CharField(max_length=50, verbose_name="Texto ferramenta destaque", default="")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return self.normal

# Model dos artigos
class Artigos(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título do artigo")
    imagem = models.ImageField(upload_to='artigos_fotos/',  blank=True, null=True)

    def __str__(self):
        return self.titulo

# Model dos vídeos
class PlataformaVideos(models.Model):
    descricao = models.TextField(verbose_name="Subtítulo")

    def __str__(self):
        return "Plataforma de vídeos"

# Model dos materiais de apoio
class MateriaisApoio(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    imagem = models.ImageField(upload_to='artigos/', blank=True, null=True)

    def __str__(self):
        return self.descricao

# Modelo dos jogos
class PlataformaJogos(models.Model):
    descricao = models.TextField(verbose_name="Subtítulo")

    def __str__(self):
        return "Plataforma de jogos digitais"
