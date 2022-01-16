from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import (
    Imovel, 
    Cidade,
    Visita
)

@login_required(login_url=reverse_lazy('entrar'))
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    cidades = Cidade.objects.all()
    if preco_minimo or preco_maximo or cidade or tipo:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']
        
        
        imoveis = Imovel.objects.filter(
            valor__range=[preco_minimo,preco_maximo],
            tipo_imovel__in=tipo,
            cidade=cidade
        )
    else:
        imoveis = Imovel.objects.all()
    
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

@login_required(login_url=reverse_lazy('entrar'))
def imovel(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    sugestoes = Imovel.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]

    return render(
        request,
        'imovel.html',
        {
            'imovel': imovel,
            'sugestoes': sugestoes,
            'id': id
        }
    )

def agendar_visitas(request):
    usuario = request.user
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')

    visita = Visita(
        imovel_id=id_imovel,
        usuario=usuario,
        dia=dia,
        horario=horario
    )
    visita.save()

    return redirect(reverse_lazy('agendamentos'))

def agendamentos(request):

    visitas = Visita.objects.filter(usuario=request.user)

    return render(
        request, 
        "agendamentos.html", 
        {
            'visitas': visitas
        }
    )

def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visita, id=id)
    visitas.status = "C"
    visitas.save()
    
    return redirect(reverse_lazy('agendamentos'))