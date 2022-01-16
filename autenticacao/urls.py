from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('entrar/', views.entrar, name="entrar"),
    path('sair/', views.sair, name="sair")
]
