# from .forms import TicketsForm
from .forms import AddTicket
from .models import Tickets
from .calculations import Calculations
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
from django.urls import reverse
from datetime import date

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TicketsSerializer
from django.utils.timezone import now
from rest_framework.views import APIView


# Create your views here.
context = {}
context['cont_ticket'] = 0



class TicektsViewSet(viewsets.ModelViewSet): #Ticket View
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = Tickets.objects.all().order_by('id')
    serializer_class = TicketsSerializer
    permission_classes = [permissions.IsAuthenticated]



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "tickets/index.html")

def add_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            
            form = AddTicket(request.POST or None)
            
            
            if form.is_valid():
                form.save()
                form.full_clean()
        form = AddTicket()
        context['page'] = 'Cadastro Ticket'
        context['form'] = form
        context['today'] = date.today().strftime("%d/%m/%Y")
        #calculations = Calculations()
        context['cont_ticket'] += 1
        #cont = calculations.calc_cont(Tickets.objects.all())
        context['protocolo'] = date.today().strftime("%Y%m%d")+ "%03d" % request.user.id + "%03d" % context['cont_ticket']
        
        
        return render(request, "tickets/add_ticket_POP.html",context)




def relatorio_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        context['page'] = 'Relatorio Ticket'
        return render(request, "tickets/relatorio_tickets.html",context)
