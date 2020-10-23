# from .forms import TicketsForm
from .forms import AddTicket
from .models import Tickets
from .models import CallFunc
from .calculations import Calculations
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from  datetime import date
from .jsonapi import Jason
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, TicketsSerializer



# Create your views here.
contUm = {}
my_list = []
contUm['cont_ticket'] = 0
class TicektsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = Tickets.objects.all().order_by('id')
    serializer_class = TicketsSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
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
