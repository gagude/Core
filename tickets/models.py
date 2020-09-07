import uuid
from django.db import models
from tasks.models import Empresas
# Create your models here.
lista = []
tp = ()

class Tickets(models.Model):  
    tp = ()
    lista = []
    def change_tp(self):
        for itens in Empresas.objects.all():
            lista.append((itens.name,itens.name))
        print(tp)
        return tuple(lista)
    tp = change_tp(lista)
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=30)
    assunto = models.CharField(max_length=30)
    data_abertura = models.DateField()
    cliente = models.CharField(max_length=30)
    responsavel = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    descri = models.CharField(max_length=500)
    protocolo = models.CharField(max_length=30)
    choicing = models.CharField(default ='Core',max_length=100,choices=tp)

    # def __init__(self, tipo, assunto, data_abertura, cliente, responsavel, status, service, descri):
    #         self.tipo = tipo
    #         self.assunto = assunto
    #         self.data_abertura = data_abertura
    #         self.cliente = cliente
    #         self.responsavel = responsavel
    #         self.status = status
    #         self.service = service
    #         self.descri = descri