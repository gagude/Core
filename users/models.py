from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# Create your models here.
CARGO = (
            ('1','Supervisor'),
            ('2','Administrador'),
            ('3','Atendente'),
        )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(verbose_name="cargo",max_length=20, choices=CARGO)
    
