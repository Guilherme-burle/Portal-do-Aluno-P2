from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Aluno

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')
        is_admin = request.POST.get('is_admin') == 'on' 

        if senha != confirmar_senha:
            return render(request, 'cadastro.html', {
                'mensagem': 'As senhas não coincidem.',
                'tipo_mensagem': 'error'
            })

        if User.objects.filter(username=nome).exists():
            return render(request, 'cadastro.html', {
                'mensagem': 'Nome de usuário já está em uso.',
                'tipo_mensagem': 'error'
            })

        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha,
            is_superuser=is_admin,
            is_staff=is_admin
        )
        user.save()

        return render(request, 'cadastro.html', {
            'mensagem': 'Cadastro realizado com sucesso!',
            'tipo_mensagem': 'success'
        })

    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')  
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'login.html')

def add_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        curso = request.POST.get('curso')
        endereco = request.POST.get('endereco')

        Aluno.objects.create(
            nome=nome,
            idade=idade,
            curso=curso,
            endereco=endereco
        )
        return redirect('homeadm')  # ou outra página de confirmação
    return render(request, 'add.html')
