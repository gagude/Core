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
    
    tipo = models.CharField("Tipo",max_length=30, blank=True, null=True)
    assunto = models.CharField("Assunto",max_length=30, blank=True, choices=lista,null=True)
    data_abertura = models.DateTimeField(blank=False)
    cliente = models.CharField(max_length=30, blank=True,null=True)
    responsavel = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=30, blank=True,null=True)
    service = models.CharField(max_length=30, blank=True,null=True)
    descri = models.CharField("Descrição",max_length=500, blank=True,null=True)
    protocolo = models.CharField(max_length=30, blank=True,null=True) 
    empresa = models.CharField(default='Core', max_length=100, blank=False)
    id_ligacao = models.CharField(max_length=40,blank=False)


class Ligacoes(models.Model):  
    
    tempo_atendimento = models.TimeField("Tempo Atendimento",auto_now=False, auto_now_add=False, blank=True, null=True)
    tempo_espera = models.TimeField("Tempo Espera",auto_now=False, auto_now_add=False, blank=True, null=True)
    data_inicio = models.DateTimeField('Data Inicio',blank=True,null=True)
    data_termino = models.DateTimeField('Data Final',blank=True,null=True)
    responsavel = models.CharField('Resposavel',max_length=50, blank=True,null=True)
    cliente = models.CharField('Cliente',max_length=50, blank=True,null=True)
    telefone = models.CharField('Telefone',max_length=50, blank=True,null=True)
    empresa = models.CharField("Empresa",max_length=50, blank=True,null=True)
    id_ligacao = models.CharField('ID Ligação',max_length=50, blank=True,null=True) 
    link = models.CharField('Link Ligação', max_length=100, blank=True,null=True)
    
