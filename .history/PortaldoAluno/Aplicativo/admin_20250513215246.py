from django.contrib import admin
from .models import Cadastro,EventoCalendario

admin.site.register(Cadastro)


from django.contrib import admin
from .models import Cadastro, EventoCalendario # Adicionado EventoCalendario

admin.site.register(Cadastro)
admin.site.register(EventoCalendario) # Registrando o novo modelo