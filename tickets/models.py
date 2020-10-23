import uuid
from django.db import models
from tasks.models import Empresas
import requests
# Create your models here.
lista = [
    ('1', 'IMPRODUTIVA'),
    ('2', 'SUPORTE'),
    ('3', 'COMERCIAL'),
    ('4', 'FINANCEIRO'),
    ('5', 'FUTURO CLIENTE'),
    ('6', 'NÃO REGISTRADO'),
    ('7', 'RECHAMADA'),]

escolhas = []
cont = 0
for itens in Empresas.objects.all():
    print(cont, itens.name)
    cont +=1
    print(cont, itens.name)
    escolhas.append((cont,itens.name))
class CallFunc():    
    def called(self):
        escolhas = []
        cont = 0
        url = 'http://192.168.0.100:8001/ticketsAPI/'  
        headers = {'Authorization': 'Token 22f4a3484716bb3fac6ac5cef67c5a81f340aec5'}
        r = requests.post(url=url,headers=headers,data={"tipo": "Teste",
        "assunto": "TesteAssunto",
        "data_abertura": "2020-10-06",
        "cliente": "TesteCliente",
        "responsavel": "Teste Responsavel",
        "status": "TEste Status",
        "service": "Teste Service",
        "descri": "DSECRIÇÃO ALEATORIA",
        "protocolo": "Protocolo Chamada",
        "empresa": "Wimax",
        "id_ligacao": "123123"}
        )
        print(r)
        for itens in Empresas.objects.all():
            cont +=1
            escolhas.append((cont,itens.name))
        
class Tickets(models.Model):  
    
    tipo = models.CharField("Tipo",max_length=30, blank=True)
    assunto = models.CharField("Assunto",max_length=30, blank=True, choices=lista)
    data_abertura = models.DateField(blank=False)
    cliente = models.CharField(max_length=30, blank=True)
    responsavel = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=30, blank=True)
    descri = models.CharField("Descrição",max_length=500, blank=False)
    protocolo = models.CharField(max_length=30, blank=False) 
    empresa = models.CharField(default='Core', max_length=100, blank=False)
    id_ligacao = models.CharField(max_length=40,blank=False)
    