from django.db import models
from . import (
    Cidade, 
    Imagem, 
    DiasVisita, 
    Horario
)

class Imovel(models.Model):
    choices = (('V', 'Venda'),
               ('A', 'Aluguel'))

    choices_imovel = (('A', 'Apartamento'),
                      ('C', 'Casa'))

    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=1, choices=choices_imovel)
    numero = models.IntegerField()
    descricao = models.TextField()
    dias_visita = models.ManyToManyField(DiasVisita)
    horarios = models.ManyToManyField(Horario)

    def __str__(self) -> str:
        return self.rua