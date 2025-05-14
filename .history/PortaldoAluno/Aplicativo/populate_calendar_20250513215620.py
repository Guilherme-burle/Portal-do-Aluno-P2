populate_calendar.py


import os
import django
from datetime import date, timedelta

# Configura o ambiente do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Projeto.settings")
django.setup()

from Aplicativo.models import EventoCalendario

def populate_calendar():
    # Limpa eventos existentes para evitar duplicatas ao rodar o script múltiplas vezes
    EventoCalendario.objects.all().delete()
    print("Eventos antigos do calendário foram removidos.")

    # Criação de dados fictícios
    eventos_data = [
        {
            "titulo": "Prova de Cálculo I",
            "data_inicio": date.today() + timedelta(days=7),
            "tipo_evento": "prova",
            "descricao": "Capítulos 1 a 3 do livro base."
        },
        {
            "titulo": "Entrega do Projeto de Algoritmos",
            "data_inicio": date.today() + timedelta(days=14),
            "tipo_evento": "entrega",
            "descricao": "Implementação do algoritmo de ordenação e relatório."
        },
        {
            "titulo": "Feriado Nacional - Dia do Trabalho",
            "data_inicio": date(date.today().year, 5, 1),
            "tipo_evento": "feriado",
        },
        {
            "titulo": "Comemoração de Aniversário da Instituição",
            "data_inicio": date.today() + timedelta(days=30),
            "data_fim": date.today() + timedelta(days=32),
            "tipo_evento": "comemoracao",
            "descricao": "Eventos culturais e palestras."
        },
        {
            "titulo": "Palestra sobre Inteligência Artificial",
            "data_inicio": date.today() + timedelta(days=5),
            "tipo_evento": "outro",
            "descricao": "Auditório principal, 14h."
        },
    ]

    for evento_info in eventos_data:
        EventoCalendario.objects.create(**evento_info)
        print(f"Evento '{evento_info['titulo']}' criado.")

    print("Dados fictícios do calendário acadêmico foram criados com sucesso!")

if _name_ == "_main_":
    populate_calendar()