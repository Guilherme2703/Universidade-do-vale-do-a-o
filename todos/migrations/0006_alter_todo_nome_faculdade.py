# Generated by Django 4.2.7 on 2023-11-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_rename_nome_campus_todo_nome_faculdade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='nome_faculdade',
            field=models.CharField(choices=[(1, 'BAIRRO CIDADE NOBRE'), (2, 'BAIRRO HORTO'), (3, 'BAIRRO VENEZA')], max_length=100),
        ),
    ]
