from msilib.schema import Class, ListView
from turtle import home
from django.shortcuts import render

from Abastecimento.models import Abastecimento, Veiculo, Funcionario, Bomba, CompraCombustivel
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views.generic.edit import CreateView


# Create your views here.
class VeiculosList(ListView):    
    model = Veiculo

class FuncionarioList(ListView):    
    model = Funcionario

class BombaList(ListView):    
    model = Bomba

class AbastecimentoList(ListView):    
    model = Abastecimento

class CompraList(ListView):    
    model = CompraCombustivel

class CreateFuncionario(CreateView):
    model = Funcionario
    fields = ['nome', 'cpf']

class CreateVeiculo(CreateView):
    model = Veiculo
    fields = ['placa', 'descricao', 'capacidadetanque']

class CreateBomba(CreateView):
    model = Bomba
    fields = ['tipocombustivel', 'capacidadebomba', 'quantidadedeestoque']

class CreateAbastecimento(CreateView):
    model = Abastecimento
    fields = ['funcionario','data', 'quantidadelitros', 'km_odometro', 'veiculo','bomba']

class CreateCompra(CreateView):
    model = CompraCombustivel
    fields = ['data', 'quantidadelitros', 'precolitro', 'bomba']

class UpdateVeiculo(UpdateView):
    model = Veiculo
    fields = ['placa', 'descricao', 'capacidadetanque']
    template_name = 'abastecimento/update.html'

class UpdateAbastecimento(UpdateView):
    model = Abastecimento
    fields = ['funcionario','data', 'quantidadelitros', 'km_odometro', 'veiculo','bomba']
    template_name = 'abastecimento/update.html'

class UpdateCompra(UpdateView):
    model = CompraCombustivel
    fields = ['data', 'quantidadelitros', 'precolitro','bomba']
    template_name = 'abastecimento/update.html'

class UpdateBomba(UpdateView):
    model = Bomba
    fields = ['tipocombustivel', 'capacidadebomba', 'quantidadedeestoque']
    template_name = 'abastecimento/update.html'

class UpdateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'cpf']
    template_name = 'abastecimento/update.html'

class DeleteFuncionario(DeleteView):
    model = Funcionario
    template_name = 'abastecimento/delete.html'

class DeleteVeiculo(DeleteView):
    model = Veiculo
    template_name = 'abastecimento/delete.html'

class DeleteAbastecimento(DeleteView):
    model = Abastecimento
    template_name = 'abastecimento/delete.html'

class DeleteBomba(DeleteView):
    model = Bomba
    template_name = 'abastecimento/delete.html'

class DeleteCompra(DeleteView):
    model = CompraCombustivel
    template_name = 'abastecimento/delete.html'
