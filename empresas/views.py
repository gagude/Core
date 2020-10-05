from django.shortcuts import render
from .forms import AddEmpresas
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
contUm = {}
def index(request):
    return HttpResponseRedirect(reverse("tasks_index"))

def add_empresas(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            
            form = AddEmpresas(request.POST or None)
            print (form)
            
            if form.is_valid():
                form.save()
                form.full_clean()
        form = AddEmpresas()
        contUm['page'] = 'Cadastro Empresa'
        contUm['form'] = form
        #calculations = Calculations()
        #cont = calculations.calc_cont(Tickets.objects.all())
       
        return render(request, "empresas/empresas.html",contUm)
    return

def relatorio_empresas(request):
    contUm['asd'] = 123 
    return render(request, "empresas/relatorio_empresas.html",contUm)

