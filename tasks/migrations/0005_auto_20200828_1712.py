# Generated by Django 3.1 on 2020-08-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200827_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='serviço',
            new_name='service',
        ),
        migrations.AddField(
            model_name='tickets',
            name='descri',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
