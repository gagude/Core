from django.shortcuts import render

# Create your views here.

from .models import NoSlugTest
from .models import SlugTest
from tickets.models import Tickets

def frontend(request, slug=None):
    """Vue.js will take care of everything else."""
    noslugtest = NoSlugTest.objects.all()
    slugtest = SlugTest.objects.all()
    ticket = Tickets.objects.all()
    
    data = {
        'articles': noslugtest,
        'authors': slugtest,
        'tickets' : ticket,
    }

    return render(request, 'vueshow/template.html', data)