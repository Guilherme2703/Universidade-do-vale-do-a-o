# Generated by Django 4.2.7 on 2023-11-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_alter_todo_nome_faculdade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='nome_faculdade',
            field=models.CharField(choices=[('BAIRRO CIDADE NOBRE', 'BAIRRO CIDADE NOBRE'), ('BAIRRO HORTO', 'BAIRRO HORTO'), ('BAIRRO VENEZA', 'BAIRRO VENEZA')], max_length=100),
        ),
    ]