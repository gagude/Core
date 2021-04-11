from .forms import AddUsers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from .models import Profile
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from datetime import date, datetime
from django.utils.timezone import now
# Create your views here.

context = {}
    
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
        print("Enter Login Page by Lack of Credentials")
        return HttpResponseRedirect(reverse("login"))
    else:
        print(request.user+"  USUARIO ENTERING ELSE")
        for itens in Profile.objects.all():
                if request.user == itens.user:
                    print("USER == ITENS USER")
                    if itens.cargo =="Supervisor":
                        print("RENDERING INDEX 2")
                        return HttpResponseRedirect(reverse("initial_page2"))
                else:
                    print("RENDERING INDEX 1")
                    return HttpResponseRedirect(reverse("initial_page"))


def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index")) 
        else:
            return render(request, "users/login.html",{
              "message":"invalid credentials"  
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message":"Logged Out" 
    })

def add_users(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            print(request.POST)

            form2 = User.objects.create_user(request.POST['login'],request.POST['email'],request.POST['password'])
            
            user = User.objects.latest('date_joined')
            user.first_name = request.POST["name"]
            user.save()
            print(request.FILES)
            data_form = {
                'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'], 
                'name': request.POST['name'], 
                'ramal': request.POST['ramal'], 
                'cargo': request.POST['cargo'], 
                'cpf': request.POST['cpf'], 
                'foto': request.FILES['foto'], 
                'banco': request.POST['banco'], 
                'agencia': request.POST['agencia'], 
                'conta': request.POST['conta'], 
                'endereco': request.POST['endereco'], 
                'email': request.POST['email'],
                'user' :  User.objects.latest('date_joined'),
                'login' : request.POST['login']
                }
            print('CHEGOU AQUI')
            form = AddUsers(data_form, request.FILES or None)
            if form.is_valid():
                form.save()
                form.full_clean()

        form = AddUsers()
        context['page'] = 'Cadastro Usuarios'
        context['form'] = form
        context['today'] = datetime.now().strftime("%d/%m/%Y")
        
        return render(request, "users/add_users.html",context)

def relatorio_users(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        print(request.user)
        if request.method == "POST":
            context['search'] = request.POST['search']
        else:
            context['search'] = '0'
        context['page'] = 'Relatorio Usuarios'
        context['my_list'] = Profile.objects.all()
        context['lista_objetos'] = len(Profile.objects.all())
        
        
        return render(request, "users/relatorio_users.html",context)