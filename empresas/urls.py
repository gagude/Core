from . import views
from django.urls import path
from tasks import views as tv
urlpatterns = [
    path("", views.index, name="index"),
    path("add_empresas", views.add_empresas, name="add_empresas"),
    path("relatorio_empresas", views.relatorio_empresas, name="relatorio_empresas"),
    path("tasks_index", tv.index, name="tasks_index"),
]