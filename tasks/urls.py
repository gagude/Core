from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_empresas, name="add_empresas"),
    path("index2", views.index2, name="index2"),
    path("ini_sup", views.ini_sup, name="ini_sup"),
    path("empresas", views.empresas, name="empresas"),
    path("relatorio_empresas", views.relatorio_empresas, name="relatorio_empresas")
]