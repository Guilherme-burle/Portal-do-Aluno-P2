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
        return self.name
    (self):
        return self.nome

class Cadastro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.user.username

class Avaliacao(models.Model):
    OPCOES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    pergunta_1 = models.CharField(max_length=3, choices=OPCOES)
    pergunta_2 = models.CharField(max_length=3, choices=OPCOES)
    pergunta_3 = models.CharField(max_length=3, choices=OPCOES)
    sugestao = models.CharField(max_length=100)

class EventoCalendario(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.data.strftime('%d/%m/%Y')}"
    
class DesempenhoFrequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    faltas = models.IntegerField()
    desempenho = models.CharField(max_length=100)  # Ex: "Excelente", "Bom", etc.
    emoji = models.CharField(max_length=5, default="🙂")  # Ex: 😃, 😐, 😞
    comentario_professor = models.TextField()

    def __str__(self):
        return f"{self.aluno.nome} - Desempenho"