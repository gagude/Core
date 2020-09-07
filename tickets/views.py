# from .forms import TicketsForm
from .forms import AddTicket
from .models import Tickets
from .calculations import Calculations
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from  datetime import date
# Create your views here.
contUm = {}
my_list = []
contUm['cont_ticket'] = 0

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "tickets/index.html")

def add_tickets(request):
    Tickets.tp = Tickets.change_tp(Tickets.lista)
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            
            form = AddTicket(request.POST or None)
            print (form)
            
            if form.is_valid():
                form.save()
                form.full_clean()
        form = AddTicket()
        contUm['page'] = 'Cadastro Ticket'
        contUm['list_size'] = len(my_list)
        contUm['form'] = form
        contUm['today'] = date.today().strftime("%d/%m/%Y")
        #calculations = Calculations()
        contUm['cont_ticket'] += 1
        #cont = calculations.calc_cont(Tickets.objects.all())
        contUm['protocolo'] = date.today().strftime("%Y%m%d")+ "%03d" % request.user.id + "%03d" % contUm['cont_ticket']
        
        
        return render(request, "tickets/add_ticket.html",contUm)

def relatorio_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        contUm['page'] = 'Relatorio Ticket'
        contUm['list_size'] = len(my_list)
        return render(request, "tickets/relatorio_tickets.html",contUm)
