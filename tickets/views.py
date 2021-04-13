# from .forms import TicketsForm
from .forms import AddTicket
from .models import Tickets, Ligacoes
from .calculations import Calculations
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
from django.urls import reverse
from datetime import date, datetime
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TicketsSerializer, LigacoesSerializer
from django.utils.timezone import now
from rest_framework.views import APIView
from users.models import Profile

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

class LigacoesViewSet(viewsets.ModelViewSet): #Ticket View
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Ligacoes.objects.all().order_by('id')
    serializer_class = LigacoesSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        print('Entering Index Tickets')
        return render(request, "tickets/index.html")

def add_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            print('Form POST')
            form = AddTicket(request.POST or None)

            if form.is_valid():

                form.save()
                form.full_clean()
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
        context['today'] = datetime.now().strftime("%d/%m/%Y")
        context['date']= datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        data_pro = datetime.now().strftime("%d%m%Y%H%M%S")
        context['responsavel'] = request.user
        context['cont_ticket'] += 1
        #cont = calculations.calc_cont(Tickets.objects.all())
        context['protocolo'] =  data_pro + str(context['cont_ticket'])

        context['user'] = request.user
        context['senha'] = context['user'].username
        context['profile_pic'] = context['user'].profile.foto
        if context['user'].profile.cargo.nome == "Atendente":
                        print('Entered index in if')
                        return render(request, "tickets/add_ticket2.html",context)
        elif context['user'].profile.cargo.nome == "Supervisor":
                
                    print('Entered index in else')
                    return render(request, "tickets/add_ticket3.html",context)
        else:
                
                    print('Entered index in else')
                    return render(request, "tickets/add_ticket.html",context)
        return render(request, "tickets/add_ticket.html",context)


def add_tickets_pop(request):
        try:
            isNumber = ''+str(request)
            isNumber = isNumber.split('?')[1]
            isNumber = isNumber.split('\'')[0]
        except:
            print('')

        if request.method == 'POST':

            form = AddTicket(request.POST or None)
            print(form.data)
            if form.is_valid():

                if not isNumber.isnumeric():
                    isNumber = form.data['id']


                if not form.data['assunto'] == '':
                    Tickets.objects.filter(id = isNumber).update(assunto = form.data['assunto'])

                if not form.data['service'] == '':
                    Tickets.objects.filter(id = isNumber).update(service = form.data['service'])

                if not form.data['tipo'] == '':
                    Tickets.objects.filter(id = isNumber).update(tipo = form.data['tipo'])

                if not form.data['descri'] == '':
                    Tickets.objects.filter(id = isNumber).update(descri = form.data['descri'])


        based = Tickets.objects.all()
        for itens in based:
                    if str(itens.id) == str(isNumber):
                        context['today'] = itens.data_abertura.strftime("%d/%m/%Y")
                        context['data_abertura'] = itens.data_abertura.strftime("%Y-%m-%dT%H:%M:%SZ")
                        context['empresa'] = itens.empresa
                        context['responsavel'] = itens.responsavel
                        context['cliente'] = itens.cliente
                        context['id_lig'] = itens.id_ligacao

        form = AddTicket()
        context['page'] = 'Cadastro Ticket'
        context['form'] = form

        #calculations = Calculations()


        context['cont_ticket'] += 1
        #cont = calculations.calc_cont(Tickets.objects.all())
        context['protocolo'] = str(context['cont_ticket']) + '000' 
        context['requestsID'] = isNumber
        if isNumber.isnumeric():
                return render(request, "tickets/add_ticket_POP.html",context)
        return render(request, "tickets/add_ticket_POP.html",context)


def relatorio_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        print(request.user)
        if request.method == "POST":
            context['search'] = request.POST['search']
        else:
            context['search'] = '0'
        context['page'] = 'Relatorio Ticket'
        context['my_list'] = Tickets.objects.all()
        context['lista_objetos'] = len(Tickets.objects.all())
        
        
        context['user'] = request.user
        if context['user'].profile.cargo.nome == "Atendente":
            return render(request, "tickets/relatorio_tickets2.html",context)
        elif context['user'].profile.cargo.nome == "Supervisor":
            return render(request, "tickets/relatorio_tickets3.html",context)
        else:
            return render(request, "tickets/relatorio_tickets.html",context)

def relatorio_tickets_view(request,arg1):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == "POST":
            print(request.POST['search'])
            context['search'] = request.POST['search']
        else:
            context['search'] = '0'
        
        context['search'] = '1'
        context['arg1'] = arg1
        context['page'] = 'Relatorio Ticket'
        context['my_list'] = Tickets.objects.all()
        counter = 0
        lista = {}
        for itens in Tickets.objects.all():
            counter += 1
            lista[counter-1] = "{% url 'relatorio_tickets_view' arg1="+counter+" %}"
        context['url_list'] = "{% url 'relatorio_tickets_view' arg1=2 %}"
        
        return render(request, "tickets/relatorio_tickets copy.html",context)