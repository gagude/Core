from events.models import Event
from events.views import evento
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddEmpresas
from .models import Empresas
from tickets.forms import AddTicket
from .calculations import Calculations
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import Profile
from tickets.models import Tickets
from tickets.models import Ligacoes
from datetime import date, datetime
# Create your views here.


context =  {}
my_list = []
#context =  Empresas.objects.get(id=8)
emps = {}
cont_tickets = 0

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        print('Entering Index Tasks')
        my_list = []
        cont_tickets = 0
        for i in Empresas.objects.all():
            try:
                my_list.append(i)
                context['my_list'] = my_list
            except:
                print('Except')
        
        context['page'] = 'DashBoard-1'
        context['user'] = request.user
        context['profile_cargo'] = request.user.profile.cargo.nome
        
        context['tickets_empresa'] = len(Tickets.objects.filter(empresa=request.user.profile.empresa))
        
        context['eventos_total'] = len(Event.objects.filter(empresa=request.user.profile.empresa))
        context['eventos_abertos'] = len(Event.objects.filter(empresa=request.user.profile.empresa, status_core="CONCLUIDO"))

        print(context['user'].profile.cargo.nome)
        print(request.user)
        print(request.user.has_perm('tickets.delete_tickets'))
        for itens in Profile.objects.all():
            if itens.user == request.user:
                context['usuario'] = itens
        
        context['list_size'] = len(my_list)
        context['receita_total'] = Calculations().total_valor(my_list)
        context['receita_total'] = Calculations().convert_money(context['receita_total'])
        context['total_chamados'] = Calculations().total_chamados(my_list)
        #FOR REAL CALCULATIONS  
        context['total_tickets'] = len(Tickets.objects.all())
        for itens in Tickets.objects.all():
            
            if(str(request.user) == str(itens.responsavel)):
                cont_tickets+=1
        context['tickets_user'] = cont_tickets
        for itens in Profile.objects.all():
             if itens.user == request.user:
                 context['senha'] = itens.user.username
        for empresas in Empresas.objects.all():
            emps[empresas.name] = empresas.contract_pack
        context['profile_pic'] = context['user'].profile.foto
        
        if context['user'].profile.cargo.nome == "Atendente":
            return render(request, "tasks/index2.html",context)
        elif context['user'].profile.cargo.nome == "Supervisor":
            return render(request, "tasks/index3.html",context)
        else:
            return render(request, "tasks/index.html",context)

        return render(request, "tasks/index.html",context)

def ini_sup(request):
    
    return render(request, "tasks/ini_sup.html")   



def chart(request):
    my_list = []
    for i in Empresas.objects.all():
        try:
            my_list.append(i)
            context['my_list'] = my_list
        except:
            print('Except')
    context['page'] = 'DashBoard-1'
    context['list_size'] = len(my_list)
    context['receita_total'] = Calculations().total_valor(my_list)
    context['receita_total'] = Calculations().convert_money(context['receita_total'])
    context['total_chamados'] = Calculations().total_chamados(my_list)
    return render(request, "tasks/chartjs.html",context)  

def add_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:

        form = AddTicket(request.POST or None)
        if form.is_valid():
            form.save()
        context['page'] = 'Ticket'
        context['list_size'] = len(my_list)
        context['form'] = form
        return render(request, "tasks/add_ticket.html",context)

def add_empresas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            
          

            data_form = {
                'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'], 
                'name': request.POST['name'], 
                'contract_pack': request.POST['contract_pack'], 
                'contract_value': request.POST['contract_value'], 
                'cnpj': request.POST['cnpj'], 
                'owner': request.POST['owner'], 
                'logo': request.FILES['logo'], 
                'start_data': request.POST['start_data'], 
                'end_contract': request.POST['end_contract'], 
                'last_renew': request.POST['last_renew'], 
                'service_level': request.POST['service_level'], 
                'excedent': request.POST['excedent'],
                'it_respon' : request.POST['it_respon']
                }
            print('CHEGOU AQUI')
            form = AddEmpresas(data_form, request.FILES or None)
            if form.is_valid():
                form.save()
                form.full_clean()

        form = AddEmpresas()
        context['page'] = 'Cadastro Empresas'
        context['form'] = form
        context['today'] = datetime.now().strftime("%d/%m/%Y")
        context['user'] = request.user
        if context['user'].profile.cargo.nome == "Supervisor":
            return render(request, "tasks/add_users3.html",context)
        else:
            return render(request, "tasks/add_empresas.html",context)

def empresas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:

        form = AddTicket(request.POST or None)
        if form.is_valid():
            form.save()
        context['page'] = 'AdicionarEmpresas'
        context['list_size'] = len(my_list)
        context['form'] = form
        return render(request, "tasks/empresas.html",context)


