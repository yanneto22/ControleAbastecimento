from msilib.schema import Class, ListView
from turtle import home
from django.shortcuts import render

from Abastecimento.models import Abastecimento, Veiculo, Funcionario, Bomba, CompraCombustivel
from django.views.generic import View, ListView
from django.http import HttpResponse


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