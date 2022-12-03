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
from Abastecimento.views import UpdateVeiculo, UpdateAbastecimento, UpdateCompra, UpdateBomba, UpdateFuncionario
from Abastecimento.views import DeleteFuncionario, DeleteAbastecimento, DeleteBomba, DeleteCompra, DeleteVeiculo


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
    path('editarveic/<int:pk>', UpdateVeiculo.as_view(success_url='/veiculos/'), name='editar_veiculo'),
    path('editarabast/<int:pk>', UpdateAbastecimento.as_view(success_url='/abastecimento/'), name='editar_abast'),
    path('editarcomp/<int:pk>', UpdateCompra.as_view(success_url='/compras/'), name='editar_compra'),
    path('editarbomba/<int:pk>', UpdateBomba.as_view(success_url='/bombas/'), name='editar_bomba'),
    path('editarfunc/<int:pk>', UpdateFuncionario.as_view(success_url='/funcionario/'), name='editar_func'),
    path('delfunc/<int:pk>', DeleteFuncionario.as_view(success_url='/funcionario/'), name='del_func'),
    path('delabastecimento/<int:pk>', DeleteAbastecimento.as_view(success_url='/abastecimento/'), name='del_abast'),
    path('delveiculo/<int:pk>', DeleteVeiculo.as_view(success_url='/veiculos/'), name='del_veiculo'),
    path('delbomba/<int:pk>', DeleteBomba.as_view(success_url='/bombas/'), name='del_bomba'),
    path('delcompra/<int:pk>', DeleteCompra.as_view(success_url='/compras/'), name='del_compra'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


