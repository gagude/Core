from django.db import models

# Create your models here.
class Empresas(models.Model):
    name = models.CharField(max_length=30)
    contract_pack = models.IntegerField()
    contract_value = models.IntegerField()
    cnpj = models.CharField(max_length=30)
    owner = models.CharField(max_length=60)
    start_data = models.DateField()
    end_contract = models.DateField()
    service_level = models.IntegerField()
    excedent = models.IntegerField()
    it_respon = models.CharField(max_length=60)

    

    
