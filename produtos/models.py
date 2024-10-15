
from django.db import models

class Equipe(models.Model):
    nome = models.CharField(verbose_name='Nome da pessoa',max_length=50)
    descricao = models.TextField()
    crp = models.CharField(verbose_name='CRP da pessoa',max_length=11,default='')
    foto = models.ImageField(default = '')