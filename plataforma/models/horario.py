from django.db import models

class Horario(models.Model):
    horario = models.TimeField()

    def __str__(self) -> str:
        return str(self.horario)