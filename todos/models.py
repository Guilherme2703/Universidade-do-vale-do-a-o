from django.db import models
from datetime import date 

produto_status = [
    ('BAIRRO CIDADE NOBRE', 'BAIRRO CIDADE NOBRE'),
    ('BAIRRO HORTO', 'BAIRRO HORTO'),
    ('BAIRRO VENEZA', 'BAIRRO VENEZA'),
]
class Todo(models.Model):
    nome_aluno = models.CharField(verbose_name="Nome do Aluno",max_length=100, null=False, blank=False)
    nome_curso =  models.CharField(verbose_name="Nome do Curso",max_length=100, null=False, blank=False)
    campi = models.CharField(verbose_name="Campus",max_length=100, choices=produto_status, null=False, blank=False)
    data_inicio = models.DateField(verbose_name="Inicio do Curso",null=False, blank=False)
    data_fim = models.DateField(verbose_name="Formatura",null=True)

    def mark_has_complete(self):
        if not self.data_fim:
            self.data_fim = date.today()
            self.save()