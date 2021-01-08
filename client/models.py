from django.db import models

# Create your models here.
tipo_list = [
    ('1','Pessoa Fisica'),
    ('2','Empresa'),
]
class Client(models.Model):  
    
    nome = models.CharField("Nome",max_length=90, blank=True, null=True)
    telefone = models.CharField("Telefone",max_length=50, blank=True, null=True)
    cpf = models.CharField('CPF',max_length=50,blank=True,null=True)
    tipo = models.CharField('Tipo',max_length=50,blank=True,null=True)
    email = models.CharField('E-mail',max_length=50, blank=True,null=True)
    endereco = models.CharField('Endereço',max_length=50, blank=True,null=True)
    bairro = models.CharField('Bairro',max_length=50, blank=True,null=True)
    cep  = models.CharField("CEP",max_length=50, blank=True,null=True)
   
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.nome