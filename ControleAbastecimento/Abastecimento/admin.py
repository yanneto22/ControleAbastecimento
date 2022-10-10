from django.contrib import admin
from Abastecimento import models

# Register your models here.
admin.site.register(models.Funcionario)
admin.site.register(models.Veiculo)
admin.site.register(models.Abastecimento)
admin.site.register(models.Bomba)
admin.site.register(models.CompraCombustivel)

