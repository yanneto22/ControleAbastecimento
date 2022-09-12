from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=200)