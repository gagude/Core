from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("add_empresas", views.add_empresas, name="add_empresas"),
    path("relatorio_empresas", views.relatorio_empresas, name="add_empresas"),
]