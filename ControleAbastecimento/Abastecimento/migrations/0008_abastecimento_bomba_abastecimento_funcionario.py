# Generated by Django 4.0.6 on 2022-12-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abastecimento', '0007_compracombustivel_bomba'),
    ]

    operations = [
        migrations.AddField(
            model_name='abastecimento',
            name='bomba',
            field=models.ManyToManyField(to='Abastecimento.bomba'),
        ),
        migrations.AddField(
            model_name='abastecimento',
            name='funcionario',
            field=models.ManyToManyField(to='Abastecimento.funcionario'),
        ),
    ]
