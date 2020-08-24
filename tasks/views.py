from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpresasForm
from .models import Empresas
from .calculations import Calculations
# Create your views here.
tasks = {"foo", "Bar", "baz"}

contUm =  {}
my_list = []
#contUm =  Empresas.objects.get(id=8)


def index(request, *args, **kwargs):
    my_list = []
    for i in range(Empresas.objects.count()):
        my_list.append(Empresas.objects.get(id=i+1))
        contUm['my_list'] = my_list
    contUm['page'] = 'DashBoard-1'
    contUm['list_size'] = len(my_list)
    return render(request, "tasks/index.html",contUm)

def empresas(request, *args, **kwargs):
    my_list = []
    
    for i in range(Empresas.objects.count()):
        my_list.append(Empresas.objects.get(id=i+1))
        contUm['my_list'] = my_list
    contUm['page'] = 'Empresas'
    calc = Calculations()
    my_list_item = calc.call_calc_unit(my_list)
    print(my_list_item)
    contUm['list_size'] = len(my_list)
    return render(request, "tasks/empresas.html",contUm)

def add_empresas(request):
    form = EmpresasForm(request.POST or None)
    if form.is_valid():
        form.save()
    contUm['page'] = 'DashBoard-1'
    contUm['list_size'] = len(my_list)
    contUm['form'] = form
    return render(request, "tasks/add_empresas.html",contUm)

def index2(request):
    return render(request, "tasks/index2.html",{
        "tasks": tasks
    })   

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