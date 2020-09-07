from django.shortcuts import render

# Create your views here.
contUm = {}
def index(request):
    return

def add_empresas(request):
    return

def relatorio_empresas(request):
    contUm['asd'] = 123 
    return render(request, "tickets/add_ticket.html",contUm)

