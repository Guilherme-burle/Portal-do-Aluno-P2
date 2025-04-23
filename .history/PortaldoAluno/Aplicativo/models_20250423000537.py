from django.contrib.auth.models import User
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    CURSOS = [
        ('programacao', 'Programação'),
        ('mecanica', 'Mecânica'),
        ('praticas', 'Práticas Administrativas'),
    ]
    curso = models.CharField(max_length=20, choices=CURSOS)
    
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Cadastro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
