from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)

class Abastecimento(models.Model):
    data = models.DateField()
    quantidadelitros = models.PositiveSmallIntegerField()
    km_odometro = models.PositiveSmallIntegerField()

class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    descricao = models.TextField()
    capacidadetanque = models.PositiveSmallIntegerField()

class Bomba(models.Model):
    tipocombustivel = models.CharField(max_length=100)
    quantidadedeestoque = models.PositiveSmallIntegerField()
    capacidadebomba = models.PositiveSmallIntegerField()

class CompraCombustivel(models.Model):
    data = models.DateField()
    quantidadelitros = models.PositiveSmallIntegerField()
    precolitro = models.DecimalField(max_digits=5, decimal_places=2)

    #teste