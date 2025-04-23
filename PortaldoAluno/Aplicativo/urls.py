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
]
