# Generated by Django 3.1.1 on 2020-11-24 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20201124_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='data_abertura',
            field=models.DateTimeField(),
        ),
    ]
