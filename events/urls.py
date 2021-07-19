from django.urls import path
from . import views as evns

urlpatterns = [
    path("", evns.eventos_index, name="eventos_index"),
    path("add_eventos", evns.add_eventos, name="add_eventos"),
    path("evento<int:my_id>", evns.evento, name="evento"),
    path("evento_status<int:my_id>", evns.evento_status, name="evento_status"),
]
