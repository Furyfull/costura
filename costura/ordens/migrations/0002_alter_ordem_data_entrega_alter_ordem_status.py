# Generated by Django 5.1.1 on 2025-01-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='data_entrega',
            field=models.DateField(verbose_name='Data de entrega'),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='status',
            field=models.IntegerField(choices=[(0, 'Não Iniciado'), (1, 'Em Andamento'), (2, 'Concluido'), (3, 'Entregue')], default=0),
        ),
    ]