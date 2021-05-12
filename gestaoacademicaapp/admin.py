from django.contrib import admin
# Register your models here.
from .models import Disciplina, Curso, Matricula
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Matricula)