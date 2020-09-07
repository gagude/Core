import uuid
from django.db import models

CHOICES= (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            )


# Create your models here.
class Empresas(models.Model):
    name = models.CharField(max_length=30)
    contract_pack = models.IntegerField()
    contract_value = models.DecimalField(max_digits=9, decimal_places=2)
    cnpj = models.CharField(max_length=30)
    owner = models.CharField(max_length=60)
    start_data = models.DateField()
    end_contract = models.DateField()
    service_level = models.CharField(default ='1',max_length=1, choices=CHOICES)
    excedent = models.DecimalField(max_digits=6, decimal_places=2)
    it_respon = models.CharField(max_length=60)

class Tickets(models.Model):
    
    u_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    tipo = models.CharField(max_length=30)
    assunto = models.CharField(max_length=30)
    data_abertura = models.DateField()
    cliente = models.CharField(max_length=30)
    responsavel = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    descri = models.CharField(max_length=500)
    protocolo =  models.CharField(max_length=30)

class Chamadas(models.Model):
    id_unico = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=30)
    data_inicio = models.CharField(max_length=30)
    data_final = models.CharField(max_length=30)
    agente = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    equipe = models.CharField(max_length=30)
    gestor = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    tempo_chamada = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    fila = models.CharField(max_length=30)
    tempo_espera = models.CharField(max_length=30)
    agente_desligou = models.CharField(max_length=30)




    
