# Generated by Django 2.0.5 on 2018-05-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20180519_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
