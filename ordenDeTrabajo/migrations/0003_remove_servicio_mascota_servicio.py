# Generated by Django 2.0.5 on 2018-07-01 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenDeTrabajo', '0002_auto_20180701_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='mascota_servicio',
        ),
    ]
