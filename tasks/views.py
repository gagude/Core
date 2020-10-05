from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpresasForm
from .forms import TicketsForm
from .models import Empresas
from .models import Tickets
from .calculations import Calculations
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import Profile
# Create your views here.
tasks = {"foo", "Bar", "baz"}

contUm =  {}
my_list = []
#contUm =  Empresas.objects.get(id=8)


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        my_list = []
        for i in Empresas.objects.all():
            try:
                my_list.append(i)
                contUm['my_list'] = my_list
            except:
                print('Except')
        contUm['page'] = 'DashBoard-1'
        contUm['list_size'] = len(my_list)
        contUm['receita_total'] = Calculations().total_valor(my_list)
        contUm['receita_total'] = Calculations().convert_money(contUm['receita_total'])
        contUm['total_chamados'] = Calculations().total_chamados(my_list)
        for itens in Profile.objects.all():
             print('Enter FOR')
             if itens.user == request.user:
                 print('Enter IF')
                 contUm['senha'] = itens.user.username
        return render(request, "tasks/index.html",contUm)

def index2(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        my_list = []
        for i in Empresas.objects.all():
            try:
                my_list.append(i)
                contUm['my_list'] = my_list
            except:
                print('Except')
        contUm['page'] = 'DashBoard-SUPERVISOR'
        contUm['list_size'] = len(my_list)
        contUm['receita_total'] = Calculations().total_valor(my_list)
        contUm['receita_total'] = Calculations().convert_money(contUm['receita_total'])
        contUm['total_chamados'] = Calculations().total_chamados(my_list)
        for itens in Profile.objects.all():
             print('Enter FOR')
             if itens.user == request.user:
                 print('Enter IF')
                 contUm['senha'] = itens.user.first_name
        return render(request, "tasks/index.html",contUm)

def empresas(request, *args, **kwargs):
    my_list = []    
    
    for i in  Empresas.objects.all():
        try:
            my_list.append(i)
            contUm['my_list'] = my_list
        except:
            print('Except')
    contUm['page'] = 'Empresas'
    calc = Calculations()
    my_list_item = calc.call_calc_unit(my_list)
    print(my_list_item)
    contUm['list_size'] = len(my_list)
    return render(request, "empresas/empresas.html",contUm)

def add_empresas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        form = EmpresasForm(request.POST or None)
        if form.is_valid():
            form.save()
        contUm['page'] = 'Cadastro Empresas'
        contUm['list_size'] = len(my_list)
        contUm['form'] = form
        print(form)
        return render(request, "empresas/empresas.html",contUm)


def ini_sup(request):
    
    return render(request, "tasks/ini_sup.html")   

def relatorio_empresas(request):
    form = EmpresasForm(request.POST or None)
    if request.POST:
        request
    contUm['page'] = 'DashBoard-1'
    contUm['list_size'] = len(my_list)
    contUm['form'] = form
    return render(request, "tasks/relatorio_empresas.html",contUm)  

def chart(request):
    my_list = []
    for i in Empresas.objects.all():
        try:
            my_list.append(i)
            contUm['my_list'] = my_list
        except:
            print('Except')
    contUm['page'] = 'DashBoard-1'
    contUm['list_size'] = len(my_list)
    contUm['receita_total'] = Calculations().total_valor(my_list)
    contUm['receita_total'] = Calculations().convert_money(contUm['receita_total'])
    contUm['total_chamados'] = Calculations().total_chamados(my_list)
    return render(request, "tasks/chartjs.html",contUm)  

def add_tickets(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:

        form = TicketsForm(request.POST or None)
        if form.is_valid():
            form.save()
        contUm['page'] = 'Ticket'
        contUm['list_size'] = len(my_list)
        contUm['form'] = form
        return render(request, "tasks/add_ticket.html",contUm)
