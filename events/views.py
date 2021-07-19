from events.foms import AddEvento, AddResposta
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Event, Image, ImageAlbum, Resposta
from tasks.models import Empresas
from datetime import date, datetime

# Create your views here.
context = {}
def eventos_index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        
        context['user'] = request.user
        context['my_list'] = Event.objects.all()
        context['my_list'] = list(reversed(context['my_list']))
        context['profile_cargo'] = request.user.profile.cargo.nome 
        context['list_client'] = Event.objects.filter(empresa=request.user.profile.empresa)
    
        context['list_client'] = list(reversed(context['list_client']))
        context['page'] = 'Lista Eventos'
        return render(request, "events/events_index.html",context)

def evento(request,my_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        
        context['user'] = request.user
        context['evento'] = Event.objects.get(id=my_id)
        if request.method == 'POST':
            images = request.FILES.getlist('images')
            form = AddResposta(request.POST or None)
            if form.is_valid():
                form.save()
                obj = None
                obj =  Resposta.objects.latest('id')
                context['evento'].resposta.add(obj) 
             #  Resposta.objects.latest('id')
                context['evento'].save()
                album_c = ImageAlbum.objects.create( )
                resposta_obj = Resposta.objects.latest('id')
                Resposta.objects.filter(id=resposta_obj.id).update(album = album_c )
               
                    
                for image in images:
                     # ImageAlbum.objects.filter(id=album_c.id).update(image = image )
                     Image.objects.create(
                         name='imagem'+str(image),
                         image = image,
                         default = True,
                         width = 100,
                         length = 100,
                         album = album_c
                     )
                
        context['user'] = request.user
        context['page'] = 'Evento'
        form = AddResposta
        context['fotos'] = Image.objects.filter(album= context['evento'].album)
        context['fotos_r'] = Image.objects.all()
            
        context['rss'] = context['evento'].resposta.all()
        context['form'] = form
        context['date']= datetime.now().strftime("%Y-%m-%d")
        context['today'] = datetime.now().strftime("%d/%m/%Y")
        return render(request, "events/event.html",context)

def evento_status(request,my_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        
        context['user'] = request.user
        context['evento'] = Event.objects.get(id=my_id)
        if request.method == 'POST':
            if request.user.profile.cargo.nome == "Cliente":
                Event.objects.filter(id=my_id).update(status_cliente = request.POST['status_core'] )
            else:
                Event.objects.filter(id=my_id).update(status_core = request.POST['status_core'] )
            return redirect('evento',my_id)
        context['user'] = request.user
        context['page'] = 'Evento'
        context['date']= datetime.now().strftime("%Y-%m-%d")
        context['today'] = datetime.now().strftime("%d/%m/%Y")
        
        return render(request, "events/event_status.html",context)


def add_eventos(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else: 
        ####### CLIENTE #########
        
            context['user'] = request.user
            context['profile_cargo'] = request.user.profile.cargo.nome 
            
            if request.method == 'POST':
                images = request.FILES.getlist('images')
                form = AddEvento(request.POST, None)
                if form.is_valid:
                    form.save()
                    album_c = ImageAlbum.objects.create( )
                    event = Event.objects.latest('id')
                    id = event.id
                    Event.objects.filter(id=event.id).update(album = album_c )
                
                        
                    for image in images:
                        # ImageAlbum.objects.filter(id=album_c.id).update(image = image )
                        Image.objects.create(
                            name='imagem'+str(image),
                            image = image,
                            default = True,
                            width = 100,
                            length = 100,
                            album = album_c
                        )
                    request.method = "GET"
                    print(request)
                    print(id)
                    return HttpResponseRedirect(reverse(eventos_index))
            context['responsavel'] = request.user
            context['empresas'] = Empresas.objects.all()
            context['page'] = 'Novo Evento'
            context['user'] = request.user 
            form = AddEvento
            context['form'] = form
            
            return render(request, "events/add_events.html",context)