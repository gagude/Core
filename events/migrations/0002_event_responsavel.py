# Generated by Django 3.2.2 on 2021-06-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='responsavel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Responsavel'),
        ),
    ]