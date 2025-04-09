from django.shortcuts import render
from django.contrib.auth.models import User

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