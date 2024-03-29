from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresas, name="empresa"),
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),
    path('excluir_empresa/<int:id>', views.excluir_empresa, name="excluir_empresa"),
    path('empresa/<int:id>', views.empresa, name="empresa_unica")
]
