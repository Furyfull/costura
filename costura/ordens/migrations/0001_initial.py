# Generated by Django 5.1.1 on 2024-10-22 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('costureiras', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('data_entrega', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Em Andamento'), (1, 'Concluido'), (2, 'Entregue')], default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordens', to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('costureira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costureiras.costureira')),
                ('ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='ordens.ordem')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servicos')),
            ],
        ),
    ]
