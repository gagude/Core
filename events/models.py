from django.db import models
from django.db.models.fields import DateField

# Create your models here.
def get_upload_path(filename):
    return f'/images/{filename}'

class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)
    name = models.CharField(max_length=13,blank=True,null=True)

    
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, null=True)

class Resposta(models.Model):
    responsavel = models.CharField("Responsavel", max_length=100,blank=True,null=True)
    resposta = models.CharField("Resposta", max_length=1000,blank=True,null=True)
    data = DateField("Data", blank=True, null=True)
    album = models.OneToOneField(ImageAlbum, related_name='resposta_model', on_delete=models.CASCADE,blank=True, null=True)

class Event(models.Model):
    parecer_cliente = models.CharField("Parecer Cliente",max_length=100,blank=True,null=True)
    parecer_core = models.CharField("Parecer Core",max_length=100,blank=True,null=True)
    status_cliente = models.CharField("Status Cliente",max_length=100,blank=True,null=True)
    status_core = models.CharField("Status Core",max_length=100,blank=True,null=True)

    empresa = models.CharField("Empresa",max_length=100,blank=True,null=True)
    relato = models.CharField('Relato',max_length=1000,blank=True,null=True)
    cpf = models.IntegerField("CPF Cliente", blank=True,null=True)
    nome_cliente = models.CharField("Nome Cliente", max_length=100, blank=True, null=True)
    data_ocorrido = models.DateField("Data Ocorrido", blank=True, null=True)
    data_relato = models.DateField("Data Relato", blank=True, null=True)
    horario = models.TimeField("Horario Ocorrido",blank=True, null=True )
    telefone = models.IntegerField("Telefone Cliente", blank=True,null=True)
    detalhes = models.CharField("Detalhes Adicionais",max_length=1000,blank=True,null=True)
    responsavel = models.CharField("Responsavel", max_length=100,blank=True,null=True)
    resposta = models.ManyToManyField(Resposta, blank=True, related_name='resposta_event')
    album = models.OneToOneField(ImageAlbum, related_name='evento_model', on_delete=models.CASCADE, blank=True, null=True)
