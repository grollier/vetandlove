# Generated by Django 2.0.5 on 2018-06-25 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordenDeTrabajo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='cliente',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='orden_cliente', to='cliente.Cliente'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='horaEntregaAproximada',
            field=models.TimeField(verbose_name='Entrega Aproximada'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='horaRecepcion',
            field=models.TimeField(verbose_name='Hora Recepcion'),
        ),
    ]
