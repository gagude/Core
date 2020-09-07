from django.urls import path
from . import views
from users import views as vs
from tickets import views as tk
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_empresas, name="add_empresas"),
    path("add_tickets", views.add_tickets, name="add_tickets"),
    path("index2", views.index2, name="index2"),
    path("ini_sup", views.ini_sup, name="ini_sup"),
    path("empresas", views.empresas, name="empresas"),
    path("relatorio_empresas", views.relatorio_empresas, name="relatorio_empresas"),
    path("logout", vs.logout_view, name="logout"),
    path("login", vs.login_view, name="login"),
    path("chart", views.chart, name="chart"),
    path("tickets_index", tk.index, name="tk_index"),
    path("tickets_rel", tk.relatorio_tickets, name="tk_rel"),
    path("tickets_add", tk.add_tickets, name="tk_add"),       
]