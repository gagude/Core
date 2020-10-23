from django.db import models

CHOICES= (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            )


# Create your models here.
class Empresas(models.Model):
    name = models.CharField(max_length=30, blank=True, )
    contract_pack = models.IntegerField(blank=True)
    contract_value = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    cnpj = models.CharField(max_length=30, blank=True)
    owner = models.CharField(max_length=60, blank=True)
    start_data = models.DateField(blank=True)
    end_contract = models.DateField(blank=True)
    service_level = models.CharField(default ='1',max_length=1, choices=CHOICES, blank=True)
    excedent = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    it_respon = models.CharField(max_length=60, blank=True)
