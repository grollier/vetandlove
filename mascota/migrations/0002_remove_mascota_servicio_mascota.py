# Generated by Django 2.0.5 on 2018-06-21 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='servicio_mascota',
        ),
    ]