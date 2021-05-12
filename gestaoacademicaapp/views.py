
from django.shortcuts import render, get_object_or_404, redirect
from .models import Disciplina, Matricula
from django.contrib.auth.decorators import login_required

@login_required
def listaMatriculas(request):

    listadisciplina = Matricula.objects.filter(estudante=request.user)
    #listadisciplina = Matricula.objects.all
    #lista a disciplina que o estudante está matriculado de acordo com o usuário que está logado.

    return render(request, 'gestaoacademicaapp/index.html', {'disciplinas':listadisciplina})

@login_required
def fazerMatricula(request, id):
    matriculardisciplina = get_object_or_404(Matricula, pk=id)

    if(matriculardisciplina.status == 'prevista'):
        matriculardisciplina.status = 'matriculado'

    matriculardisciplina.save()

    return redirect('/')