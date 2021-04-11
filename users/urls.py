from django.urls import path
from . import views
from tasks import views as ts

urlpatterns = [
    path("", ts.index, name="index"),
    path("index", ts.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("add", views.add_users, name="add_users"),
    path("rel", views.relatorio_users, name="rel_users")
]