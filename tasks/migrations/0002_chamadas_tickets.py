# Generated by Django 3.0.8 on 2020-08-27 03:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamadas',
            fields=[
                ('id_unico', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
                ('data_inicio', models.CharField(max_length=30)),
                ('data_final', models.CharField(max_length=30)),
                ('agente', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=30)),
                ('equipe', models.CharField(max_length=30)),
                ('gestor', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('tempo_chamada', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=30)),
                ('fila', models.CharField(max_length=30)),
                ('tempo_espera', models.CharField(max_length=30)),
                ('agente_desligou', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('protocolo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
                ('assunto', models.CharField(max_length=30)),
                ('data_abertura', models.DateField()),
                ('cliente', models.CharField(max_length=30)),
                ('responsavel', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('serviço', models.CharField(max_length=30)),
            ],
        ),
    ]
