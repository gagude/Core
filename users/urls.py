from django.urls import path
from . import views
from tasks import views as ts

urlpatterns = [
    path("", ts.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]