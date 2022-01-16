from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def cadastrar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastrar.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect(reverse_lazy('cadastrar'))

        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
            return redirect(reverse_lazy('cadastrar'))
        try:
            user = User.objects.create_user(
                username=username,                  
                email=email,
                password=senha
            )
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect(reverse_lazy('entrar'))
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')

            return redirect(reverse_lazy('cadastrar'))
        

def entrar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse_lazy('entrar'))

        return render(request, 'entrar.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse_lazy('entrar'))
        else:
            auth.login(request, usuario)
            return redirect(reverse_lazy('home'))

def sair(request):
    auth.logout(request)
    return redirect(reverse_lazy('entrar'))