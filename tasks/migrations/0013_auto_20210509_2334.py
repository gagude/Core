# Generated by Django 3.1.1 on 2021-05-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20210509_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresas',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='excedent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Valor Excedente'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='it_respon',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Responsavel TI'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='service_level',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=1, null=True, verbose_name='Nivel de Serviço'),
        ),
    ]