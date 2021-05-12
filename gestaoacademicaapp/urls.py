from django.urls import path
from . import views
"""todas as urls referente a gestãoacademica deverão estar nesse aquivo"""
urlpatterns = [
 path('', views.listaMatriculas, name='lista-disciplinamatricula'),
 path('fazerMatricula/<int:id>', views.fazerMatricula, name="alterarstatusmatricula"),
]
