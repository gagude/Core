# Generated by Django 3.2.2 on 2021-06-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210628_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagealbum',
            name='name',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
