from django.db import models

class Cadastro(models.Model):
    nome = models.TextField(max_length=100, default='usuario_temp')
    email = models.EmailField(default='temp@email.com')
    senha = models.CharField(max_length=100, default='senha123')

    def __str__(self):
        return self.nome
    
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
