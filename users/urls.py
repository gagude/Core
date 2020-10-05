from django.urls import path
from . import views
from tasks import views as vs

urlpatterns = [
    path("", vs.index, name="initial_page"),
    path("initial_page2", vs.index2, name="initial_page2"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]