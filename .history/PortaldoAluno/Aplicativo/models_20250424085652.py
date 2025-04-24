from django.contrib.auth.models import User
from django.db import models

class Aluno(models.Model):
    ESCOLARIDADE_CHOICES = [
        ('medio-incompleto', 'Ensino médio incompleto'),
        ('medio-completo', 'Ensino médio completo'),
        ('superior-andamento', 'Ensino superior em andamento'),
    ]

    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]

    CURSOS = [
        ('programacao', 'Programação'),
        ('mecanica', 'Mecânica'),
        ('praticas-administrativas', 'Práticas Administrativas'),
    ]

    nome = models.CharField(max_length=100) 
    data_nascimento = models.DateField()
    escolaridade = models.CharField(max_length=30, choices=ESCOLARIDADE_CHOICES)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    escola = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    curso = models.CharField(max_length=30, choices=CURSOS)

    def __str__(self):
        return self.nome

class Cadastro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
