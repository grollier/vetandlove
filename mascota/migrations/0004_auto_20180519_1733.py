# Generated by Django 2.0.5 on 2018-05-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20180519_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, verbose_name='Altura'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, verbose_name='Peso'),
        ),
    ]
