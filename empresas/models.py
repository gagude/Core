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
