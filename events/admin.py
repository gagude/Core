from events.models import Event
from django.contrib import admin
from .models import Event, Image, ImageAlbum, Resposta
# Register your models here.

admin.site.register(Event)
admin.site.register(Resposta)
admin.site.register([ImageAlbum, Image])


