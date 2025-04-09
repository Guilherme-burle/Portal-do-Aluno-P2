from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.TextField(max_length=100, default='usuario_temp')
    email = models.EmailField(default='temp@email.com')
    senha = models.CharField(max_length=100, default='senha123')

    def __str__(self):
        return self.nome