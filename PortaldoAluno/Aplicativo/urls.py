from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('add/', views.add_aluno, name='add_aluno'),
    path('homeadm/', views.home_adm, name='homeadm'),
    path('excluir/<int:aluno_id>/', views.excluir_aluno, name='excluir'),

]
