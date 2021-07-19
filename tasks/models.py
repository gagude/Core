import uuid
from django.db import models

CHOICES= (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            )


# Create your models here.
class Empresas(models.Model):
    name = models.CharField("Nome",max_length=300, blank=True, null=True)
    cidade = models.CharField("Cidade",max_length=300, blank=True, null=True)
    estado = models.CharField("Estado",max_length=2, blank=True, null=True)
    endereco = models.CharField("Endereço",max_length=300, blank=True, null=True)
    contract_pack = models.IntegerField("Pacote Atendimentos",blank=True, null=True, default=0)
    contract_value = models.DecimalField("Valor Pacote",max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    cnpj = models.CharField("CNPJ",max_length=30, blank=True, null=True)
    owner = models.CharField("Responsanvel",max_length=60, blank=True, null=True)
    start_data = models.DateField("Data Entrada",blank=True, null=True)
    end_contract = models.DateField("Fim contrato",blank=True, null=True)
    last_renew = models.DateField("Ultima Renovação",blank=True, null=True)
    service_level = models.CharField("Nivel de Serviço",default ='1',max_length=1, choices=CHOICES, blank=True, null=True)
    excedent = models.DecimalField("Valor Excedente",max_digits=6, decimal_places=2, blank=True, null=True, default=0)
    it_respon = models.CharField("Responsavel TI",max_length=60, blank=True, null=True)
    logo = models.ImageField("Logo",upload_to='static/images/', null=True,blank= True)
    def __str__(self):
        return '%s' % self.name
        
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


    
