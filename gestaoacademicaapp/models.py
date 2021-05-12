from django.db import models
from django.contrib.auth import get_user_model
class Curso(models.Model):
 titulo = models.CharField(max_length=255)
 descricao = models.TextField(),
 datacriacao = models.DateTimeField(auto_now_add=True)
 def __str__(self):
      return self.titulo
class Disciplina(models.Model):
 STATUS = (
 ('ativa', 'Ativa'),
 ('desativada', 'Desativada'),
 )
 titulo = models.CharField(max_length=255, blank=True, null=True)
 turno = models.CharField(max_length=10, blank=True, null=True)
 diadasemana = models.CharField(max_length=20, blank=True, null=True)
 local = models.CharField(max_length=20, blank=True, null=True)
 descricao = models.TextField()
 status = models.CharField(
 max_length=11,
 choices=STATUS,
 )
 estudante = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
 curso = models.ForeignKey('Curso', verbose_name="Cursos", on_delete=models.CASCADE, blank=True, null=True)
 datacriacao = models.DateTimeField(auto_now_add=True)
 def __str__(self):
  return f"{self.curso},{self.titulo},{self.turno},{self.diadasemana}"
class Matricula(models.Model):
 STATUS = (
 ('matriculado', 'Em andamento'),
 ('prevista', 'Prevista'),
 ('aprovado', 'Aprovado'),
 ('dependencia', 'Dependência'),
 )
 semestre = models.CharField(max_length=255)
 status = models.CharField(
 max_length=12,
 choices=STATUS,
 )
 estudante = models.ForeignKey(get_user_model(), related_name='+', on_delete=models.CASCADE)
 disciplina = models.ForeignKey('Disciplina', verbose_name="Disciplinas",
related_name="disciplinafk", on_delete=models.CASCADE)
 datacriacao = models.DateTimeField(auto_now_add=True)
 def __str__(self):
  return f"{self.estudante},{self.disciplina},{self.semestre},{self.status}"