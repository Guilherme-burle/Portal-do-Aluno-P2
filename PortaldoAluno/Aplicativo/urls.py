from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('add/', views.add_aluno, name='add'),
    path('homeadm/', views.home_adm, name='homeadm'),
    path('ver/', views.ver, name='ver'),
    path('ver/<int:aluno_id>/deletar', views.deletar_alunos, name='deletar'),
    path('ver/<int:aluno_id>/editar', views.editar_alunos, name='editar'),
    path('avaliacao', views.avaliar_solidare, name='avaliacao'),
]
