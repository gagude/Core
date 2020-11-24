# Generated by Django 3.1.1 on 2020-11-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20201124_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='assunto',
            field=models.CharField(blank=True, choices=[('1', 'IMPRODUTIVA'), ('2', 'SUPORTE'), ('3', 'COMERCIAL'), ('4', 'FINANCEIRO'), ('5', 'FUTURO CLIENTE'), ('6', 'NÃO REGISTRADO'), ('7', 'RECHAMADA'), ('8', 'Teste')], max_length=30, null=True, verbose_name='Assunto'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='cliente',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='descri',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='protocolo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='service',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo'),
        ),
    ]