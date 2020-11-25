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
            print('Form POST')
            form = AddTicket(request.POST or None)

            if form.is_valid():
                print('Form Valid')
                form.save()
                form.full_clean()
            else:
                print("NÃO")
        try:
            isNumber = ''+str(request)
            isNumber = isNumber.split('?')[1]
            isNumber = isNumber.split('\'')[0]
        except:
            print(isNumber+'Is Not a Number')
        
        form = AddTicket()
        context['page'] = 'Cadastro Ticket'
        context['form'] = form
        
        #calculations = Calculations()
        context['today'] = date.today().strftime("%Y-%m-%d")
        context['responsavel'] = request.user
        context['cont_ticket'] += 1
        #cont = calculations.calc_cont(Tickets.objects.all())
        context['protocolo'] = date.today().strftime("%Y%m%d")+ "%03d" % request.user.id + "%03d" % context['cont_ticket']
        context['requestsID'] = isNumber
        if isNumber.isnumeric():
                print('NUMERO')
                based = Tickets.objects.all()
                for itens in based:
                    if str(itens.id) == str(isNumber):
                        context['today'] = itens.data_abertura
                        context['empresa'] = itens.empresa
                        context['responsavel'] = itens.responsavel
                        context['cliente'] = itens.cliente

                return render(request, "tickets/add_ticket_POP.html",context)
        return render(request, "tickets/add_ticket.html",context)


def add_tickets_pop(request):
        try:
            isNumber = ''+str(request)
            isNumber = isNumber.split('?')[1]
            isNumber = isNumber.split('\'')[0]
        except:
            print(isNumber+'Is Not a Number')

        if request.method == 'POST':
            print('Form POST')
            form = AddTicket(request.POST or None)
            print(form.data)
            if form.is_valid():
                print('Form Valid')
                if not isNumber.isnumeric():
                    isNumber = form.data['id']
                Tickets.objects.filter(id = isNumber).update(assunto = form.data['assunto'])
                Tickets.objects.filter(id = isNumber).update(service = form.data['service'])
                Tickets.objects.filter(id = isNumber).update(tipo = form.data['tipo'])
                Tickets.objects.filter(id = isNumber).update(status = form.data['status'])
                Tickets.objects.filter(id = isNumber).update(descri = form.data['descri'])

        based = Tickets.objects.all()
        for itens in based:
                    if str(itens.id) == str(isNumber):
                        context['today'] = itens.data_abertura.strftime("%Y%m%d")
                        context['data_abertura'] = itens.data_abertura
                        context['empresa'] = itens.empresa
                        context['responsavel'] = itens.responsavel
                        context['cliente'] = itens.cliente
                        context['id_lig'] = itens.id_ligacao

        form = AddTicket()
        context['page'] = 'Cadastro Ticket'
        context['form'] = form
        print()
        #calculations = Calculations()
        
        
        context['cont_ticket'] += 1
        #cont = calculations.calc_cont(Tickets.objects.all())
        context['protocolo'] = date.today().strftime("%Y%m%d")+ "%03d" % request.user.id + "%03d" % context['cont_ticket']
        context['requestsID'] = isNumber
        if isNumber.isnumeric():
                print('NUMERO')
                

                return render(request, "tickets/add_ticket_POP.html",context)
        return render(request, "tickets/add_ticket_POP.html",context)
        

def relatorio_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        context['page'] = 'Relatorio Ticket'
        return render(request, "tickets/relatorio_tickets.html",context)
