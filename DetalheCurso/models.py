from django.db import models

class DetalheCurso(models.Model):
    codigoCurso = models.CharField(max_length=100)
    codigoTurma = models.CharField(max_length=100)
