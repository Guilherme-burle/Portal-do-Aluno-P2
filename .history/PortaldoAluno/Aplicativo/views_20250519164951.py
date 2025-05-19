from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .models import Aluno, Avaliacao, EventoCalendario, DesempenhoFrequencia
from django.contrib import messages
from django.urls import reverse
from .decorators import login_required
from django.contrib.auth.hashers import make_password
from datetime import date


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def home_adm(request):
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
                first_name=nome,  
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
            print("Dados inválidos") 
            return render(request, 'login.html', {'erro': 'Dados inválidos'})
    
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  

@login_required
def add_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        escolaridade = request.POST.get('escolaridade')
        turno = request.POST.get('turno')
        escola = request.POST.get('escola')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        curso = request.POST.get('curso')

        if not all([nome, data_nascimento, escolaridade, turno, escola, endereco, bairro, telefone, curso]):
            return render(request, 'add.html', {'erro': 'Todos os campos são obrigatórios'})

        aluno = Aluno.objects.create(
            nome=nome,
            data_nascimento=data_nascimento,
            escolaridade=escolaridade,
            turno=turno,
            escola=escola,
            endereco=endereco,
            bairro=bairro,
            telefone=telefone,
            curso=curso,
        )

        aluno.save()

        messages.success(request, 'Aluno cadastrado com sucesso!')
        return render(request, 'add.html')

    return render(request, 'add.html')

@login_required
def ver(request):
    alunos = Aluno.objects.all()

    return render(request, 'ver.html', {'alunos': alunos})

@login_required
def deletar_alunos(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.delete()
    return redirect(request.META.get('HTTP_REFERER', 'ver'))

@login_required
def editar_alunos(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        escolaridade = request.POST.get('escolaridade')
        turno = request.POST.get('turno')
        escola = request.POST.get('escola')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        telefone = request.POST.get('telefone')
        curso = request.POST.get('curso')

        alterado = (
            nome != aluno.nome or
            data_nascimento != str(aluno.data_nascimento) or
            escolaridade != aluno.escolaridade or
            turno != aluno.turno or
            escola != aluno.escola or
            endereco != aluno.endereco or
            bairro != aluno.bairro or
            telefone != aluno.telefone or
            curso != aluno.curso
        )

        if alterado:
            aluno.nome = nome
            aluno.data_nascimento = data_nascimento
            aluno.escolaridade = escolaridade
            aluno.turno = turno
            aluno.escola = escola
            aluno.endereco = endereco
            aluno.bairro = bairro
            aluno.telefone = telefone
            aluno.curso = curso
            aluno.save()
            messages.success(request, 'Informações atualizadas com sucesso!')
        else:
            messages.error(request, 'Você precisa alterar alguma informação.')

    return render(request, 'editar.html', {'aluno': aluno})

@login_required
def avaliar_solidare(request):
    if request.method == 'POST':
        pergunta_1 = request.POST.get('pergunta_1')
        pergunta_2 = request.POST.get('pergunta_2')
        pergunta_3 = request.POST.get('pergunta_3')
        sugestao = request.POST.get('sugestao', '')

        if not all([pergunta_1, pergunta_2, pergunta_3]):
            messages.error(request, 'Responda todos os campos.')
            return render(request, 'avaliacao.html')

        Avaliacao.objects.create(
            pergunta_1=pergunta_1,
            pergunta_2=pergunta_2,
            pergunta_3=pergunta_3,
            sugestao=sugestao
        )
        messages.success(request, 'Avaliação enviada com sucesso!')

    return render(request, 'avaliacao.html')

@login_required
def calendario(request):
    hoje = date.today()
    eventos = EventoCalendario.objects.filter(user=request.user).order_by('data')
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    contexto = {
        'meses': meses,
        'dias_semana': dias_semana,
        'eventos': eventos,
        'ano_atual': hoje.year,
        'mes_atual': hoje.month - 1  
    }
    return render(request, 'calendario.html', contexto)

@login_required
def add_eventos(request):
    data = request.GET.get('data')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        horario = request.POST.get('horario')


        if nome and data:
            EventoCalendario.objects.create(nome=nome, data=data, horario=horario, user=request.user)
            messages.success(request, "Evento adicionado com sucesso!")
            return redirect('calendario')
        else:
            return render(request, 'add_eventos.html', {'erro': 'Dados incompletos.', 'data': data}) 

    if not data:
        return render(request, 'erro.html', {'mensagem': 'Data não informada.'})

    return render(request, 'add_eventos.html', {'data': data})

@login_required
def addD(request):
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        faltas = request.POST.get('faltas')
        desempenho = request.POST.get('desempenho')
        emoji = request.POST.get('emoji')
        comentario = request.POST.get('comentario_professor')

        aluno = get_object_or_404(Aluno, id=aluno_id)

        DesempenhoFrequencia.objects.create(
            aluno=aluno,
            faltas=faltas,
            desempenho=desempenho,
            emoji=emoji,
            comentario_professor=comentario
        )
        return redirect('desempenho_list')

    alunos = Aluno.objects.all()
    return render(request, 'desempenho_create.html', {'alunos': alunos})

@login_required
def desempenho_list(request):
    desempenhos = DesempenhoFrequencia.objects.select_related('aluno').all()
    return render(request, 'desempenho_list.html', {'desempenhos': desempenhos})

@login_required
def desempenho_edit(request, id):
    desempenho = get_object_or_404(DesempenhoFrequencia, id=id)

    if request.method == 'POST':
        desempenho.faltas = request.POST.get('faltas')
        desempenho.desempenho = request.POST.get('desempenho')
        desempenho.emoji = request.POST.get('emoji')
        desempenho.comentario_professor = request.POST.get('comentario_professor')
        desempenho.save()
        return redirect('desempenho_list')

    return render(request, 'desempenho_edit.html', {'desempenho': desempenho})

@login_required
def desempenho_delete(request, id):
    desempenho = get_object_or_404(DesempenhoFrequencia, id=id)
    desempenho.delete()
    return redirect('desempenho_list')