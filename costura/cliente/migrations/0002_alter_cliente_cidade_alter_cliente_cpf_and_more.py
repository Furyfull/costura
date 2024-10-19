# Generated by Django 5.1.1 on 2024-10-19 20:15

import django_cpf_cnpj.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
