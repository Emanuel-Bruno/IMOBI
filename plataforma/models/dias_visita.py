from django.db import models

class DiasVisita(models.Model):
    dia = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.dia