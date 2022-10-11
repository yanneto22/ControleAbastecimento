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
    fields = ['tipocombustivel', 'capacidadebomba']

class CreateAbastecimento(CreateView):
    model = Abastecimento
    fields = ['data', 'quantidadelitros', 'km_odometro']

class CreateCompra(CreateView):
    model = CompraCombustivel
    fields = ['data', 'quantidadelitros', 'precolitro']