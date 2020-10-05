from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from .models import Profile
# Create your views here.


    

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
            print(str(request.user)+"  USUARIO ENTERING ELSE")
            for itens in Profile.objects.all():
                print('Runing for One More Time')
                if request.user == itens.user:
                    print("USER == ITENS USER")
                    if itens.cargo =="Supervisor":
                        print("RENDERING INDEX 2")
                        return HttpResponseRedirect(reverse("initial_page2"))
            else:
                print("RENDERING INDEX 1")
                return HttpResponseRedirect(reverse("initial_page"))     
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