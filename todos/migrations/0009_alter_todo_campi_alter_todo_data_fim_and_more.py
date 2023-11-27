# Generated by Django 4.2.7 on 2023-11-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_rename_nome_faculdade_todo_campi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='campi',
            field=models.CharField(choices=[('BAIRRO CIDADE NOBRE', 'BAIRRO CIDADE NOBRE'), ('BAIRRO HORTO', 'BAIRRO HORTO'), ('BAIRRO VENEZA', 'BAIRRO VENEZA')], max_length=100, verbose_name='Campus'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='data_fim',
            field=models.DateField(null=True, verbose_name='Formatura'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='data_inicio',
            field=models.DateField(verbose_name='Inicio do Curso'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='nome_aluno',
            field=models.CharField(max_length=100, verbose_name='Nome do Aluno'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='nome_curso',
            field=models.CharField(max_length=100, verbose_name='Nome do Curso'),
        ),
    ]
