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
    path('avaliacao/', views.avaliar_solidare, name='avaliacao'),
    path('calendario/', views.calendario, name='calendario'),
    path('add_eventos/', views.add_eventos, name='add_eventos'),
    path('desempenhos/', views.desempenho_list, name='desempenho_list'),
    path('desempenhos/novo/', views.desempenho_create, name='desempenho_create'),
    path('desempenhos/<int:pk>/', views.desempenho_detail, name='desempenho_detail'),
    path('desempenhos/<int:pk>/editar/', views.desempenho_update, name='desempenho_update'),
    path('desempenhos/<int:pk>/excluir/', views.desempenho_delete, name='desempenho_delete'),
]


