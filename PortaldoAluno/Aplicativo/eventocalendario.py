from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('Aplicativo', '0003_avaliacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoCalendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('tipo_evento', models.CharField(choices=[('prova', 'Prova'), ('entrega', 'Entrega de Trabalho'), ('feriado', 'Feriado'), ('comemoracao', 'Comemoração'), ('outro', 'Outro')], max_length=20)),
            ],
            options={
                'ordering': ['data_inicio'],
            },
        ),
    ]