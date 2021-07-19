from django import template
from events.models import Image,ImageAlbum
register = template.Library()


@register.filter
def lower(value):
    
    return Image.objects.filter(album= value.album)