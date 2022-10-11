"""ControleAbastecimento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Abastecimento.views import CreateAbastecimento, CreateBomba, CreateCompra, CreateFuncionario, CreateVeiculo, VeiculosList, FuncionarioList, BombaList, AbastecimentoList, CompraList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/', VeiculosList.as_view(), name='veiculo_list'),
    path('funcionario/', FuncionarioList.as_view(), name='funcionario_list'),
    path('bombas/', BombaList.as_view(), name='bomba_list'),
    path('abastecimento/', AbastecimentoList.as_view(), name='abastecimento_list'),
    path('compras/', CompraList.as_view(), name='compra_list'),
    path('criarfunc/', CreateFuncionario.as_view(success_url='/funcionario/'), name='criar_func'),
    path('criarveic/', CreateVeiculo.as_view(success_url='/veiculos/'), name='criar_veic'),
    path('criarbomba/', CreateBomba.as_view(success_url='/bombas/'), name='criar_bomba'),
    path('criarabast/', CreateAbastecimento.as_view(success_url='/abastecimento/'), name='criar_abast'),
    path('criarcompra/', CreateCompra.as_view(success_url='/compras/'), name='criar_compra'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


