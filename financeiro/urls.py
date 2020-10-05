from . import views
from django.urls import path
from tasks import views as tv

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks_index", tv.index, name="tasks_index"),
]