# Generated by Django 3.1.1 on 2020-10-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20200915_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='choicing',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='u_id',
        ),
        migrations.AddField(
            model_name='tickets',
            name='empresa',
            field=models.CharField(choices=[(1, 'Wimax'), (2, 'R2 Telecom'), (3, 'Telecall'), (4, 'Proxer'), (5, 'Cambuhy'), (6, 'Sothis')], default='Core', max_length=100),
        ),
        migrations.AddField(
            model_name='tickets',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets',
            name='id_ligação',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickets',
            name='assunto',
            field=models.CharField(blank=True, choices=[('1', 'IMPRODUTIVA'), ('2', 'IMPRODUTIVA2'), ('3', 'IMPRODUTIVA3'), ('4', 'IMPRODUTIVA4'), ('5', 'IMPRODUTIVA5'), ('6', 'IMPRODUTIVA6'), ('7', 'IMPRODUTIVA7'), ('8', 'IMPRODUTIVA8')], max_length=30, verbose_name='Assunto'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='cliente',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='descri',
            field=models.CharField(blank=True, max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, verbose_name='Tipo'),
        ),
    ]
