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
    ('7', 'RECHAMADA'),
    ('8', 'Teste'),]

class Tickets(models.Model):  
    
    tipo = models.CharField("Tipo",max_length=30, blank=True)
    assunto = models.CharField("Assunto",max_length=30, blank=True, choices=lista)
    data_abertura = models.DateField(blank=False)
    cliente = models.CharField(max_length=30, blank=True)
    responsavel = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=30, blank=True)
    descri = models.CharField("Descrição",max_length=500, blank=True)
    protocolo = models.CharField(max_length=30, blank=True) 
    empresa = models.CharField(default='Core', max_length=100, blank=False)
    id_ligacao = models.CharField(max_length=40,blank=False)

