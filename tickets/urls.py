from django.urls import path
from . import views
from users import views as vs

urlpatterns = [
    path("", views.index, name="index"),
    path("add_tickets", views.add_tickets, name="add_tickets"),
    path("relatorio_tickets", views.relatorio_tickets, name="relatorio_tickets"),
    path("logout", vs.logout_view, name="logout"),
    path("login", vs.login_view, name="login"),
]