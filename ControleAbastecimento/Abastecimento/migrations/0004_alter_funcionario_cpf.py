# Generated by Django 4.0.6 on 2022-11-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abastecimento', '0003_veiculo_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
