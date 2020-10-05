from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse("index"))

def cadastro(request):
    return HttpResponseRedirect(reverse("index"))

def relatorio(request):
    return HttpResponseRedirect(reverse("index"))