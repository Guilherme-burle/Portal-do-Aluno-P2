from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .models import Aluno
from .decorators import login_required 


def home(request):
    return render(request, 'home.html')

@login_required
def home_adm(request):
    return render(request, 'homeadm.html')

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
            return redirect('homeadm') if user.is_staff else redirect('home')
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
        return redirect('homeadm')  
    if not all([nome, idade, curso, endereco]):
        return render(request, 'add.html', {'erro': 'Todos os campos são obrigatórios'})


@login_required
def excluir_aluno(request, aluno_id=None):
    if aluno_id:
        aluno = get_object_or_404(Aluno, id=aluno_id)
        aluno.delete()
        return redirect('excluir_aluno')

    alunos = Aluno.objects.all()
    return render(request, 'excluirAluno.html', {'alunos': alunos})

