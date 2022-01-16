from django.db import models
from django.contrib.auth.models import User
from .imovel import Imovel

class Visita(models.Model):
    choices = (
        ('S', 'Segunda'),
        ('T', 'Terça'),
        ('Q', 'Quarta'),
        ('QI', 'Quinta'),
        ('SE', 'Sexta'),
        ('SA', 'Sabado'),
        ('D', 'Domingo')
    )

    choices_status = (
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado')
    )

    imovel = models.ForeignKey(Imovel, on_delete=models.DO_NOTHING)

    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    dia = models.CharField(max_length=20)

    horario = models.TimeField()

    status = models.CharField(max_length=1, choices=choices_status, default="A")

    def __str__(self) -> str:
        return self.usuario.username