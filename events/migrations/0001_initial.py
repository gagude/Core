# Generated by Django 3.2.2 on 2021-06-24 13:49

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(blank=True, max_length=100, null=True, verbose_name='Empresa')),
                ('relato', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Relato')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF')),
                ('nome_cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Cliente')),
                ('data_ocorrido', models.DateField(blank=True, null=True, verbose_name='Data Ocorrido')),
                ('data_relato', models.DateField(blank=True, null=True, verbose_name='Data Ocorrido')),
                ('horario', models.TimeField(blank=True, null=True, verbose_name='Horario Ocorrido')),
                ('telefone', models.IntegerField(blank=True, null=True, verbose_name='Telefone Cliente')),
                ('detalhes', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Detalhes Adicionais')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(blank=True, max_length=100, null=True, verbose_name='Responsavel')),
                ('resposta', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Resposta')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resposta_model', to='events.imagealbum')),
                ('evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resposta_event', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=events.models.get_upload_path)),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.imagealbum')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='evento_model', to='events.imagealbum'),
        ),
    ]
