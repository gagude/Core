from tasks.models import Empresas
from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# Create your models here.
CARGO = (
            ('1','Supervisor'),
            ('2','Administrador'),
            ('3','Atendente'),
            ('4','Cliente'),
        )
class Cargo(models.Model):
    nome = models.CharField(max_length=30)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    carga_horaria = models.IntegerField()
    def __str__(self):
        return '%s' % self.nome
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank= True)
    ramal = models.CharField('Agente',max_length=30,blank= True) # Ramal vindo do sistema parceiro para identificação de agente
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT,blank= True)
    cpf = models.IntegerField("CPF",blank= True)
    banco = models.CharField("Banco", max_length=30,blank= True)
    agencia = models.IntegerField("Agência",blank= True)
    conta = models.IntegerField("Conta",blank= True)
    endereco = models.CharField("Endereço", max_length=250,blank= True)
    foto = models.ImageField("Foto",upload_to='static/images/', null=True,blank= True)
    telefone = models.CharField("Telefone", max_length=11,blank= True)
    empresa = models.ForeignKey(Empresas,  related_name='images', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '%s' % self.user
    # Contatos
    # Problemas de Saúde 