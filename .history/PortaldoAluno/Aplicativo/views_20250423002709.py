from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .models import Aluno
from .decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def home_administrador(request):
    alunos = Aluno.objects.all()  
    return render(request, 'homeadm.html', {'alunos': alunos})


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        is_admin = request.POST.get('is_admin') == 'on' 

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"Senha: {senha}")
        print(f"Administrador: {is_admin}")

        if User.objects.filter(email=email).exists():  
            return render(request, 'cadastro.html', {'mensagem': 'E-mail já está em uso.'})
        
        try:
            user = User.objects.create_user(
                username=email,  
                email=email,
                password=senha,
                is_superuser=is_admin,
                is_staff=is_admin
            )
            user.save()

            print(f"Usuário {user.username} cadastrado com sucesso!")
            
            return redirect('login')

        except Exception as e:
            print(f"Erro ao criar o usuário: {e}")
            return render(request, 'cadastro.html', {
                'mensagem': 'Erro ao cadastrar o usuário. Tente novamente.',
                'tipo_mensagem': 'error'
            })

    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"Username: {username}, Password: {password}")  
        user = authenticate(request, username=username, password=password)
        
        if user:
            print("Usuário autenticado!") 
            auth_login(request, user)
            return redirect('homeadm') if user.is_staff else redirect('home')
        else:
            print("Credenciais inválidas") 
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})
    
    return render(request, 'login.html')


@login_required
def add_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        curso = request.POST.get('curso')
        endereco = request.POST.get('endereco')

        if not all([nome, idade, curso, endereco]):
            return render(request, 'add.html', {'erro': 'Todos os campos são obrigatórios'})

        Aluno.objects.create(
            nome=nome,
            idade=idade,
            curso=curso,
            endereco=endereco
        )
        return redirect('homeadm')

    return render(request, 'add.html')

@login_required
def excluir_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.delete()
    
    # Após a exclusão, redireciona para a página de administração
    return redirect('homeadm')
