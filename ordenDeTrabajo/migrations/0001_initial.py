# Generated by Django 2.0.5 on 2018-05-07 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('detalleId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Nueva', 'NUEVA'), ('Activa', 'ACTIVA'), ('Finalizada', 'FINALIZADA'), ('Cancelada', 'CANCELADA')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('ordenId', models.AutoField(primary_key=True, serialize=False)),
                ('numeroOrden', models.PositiveIntegerField(default='0000', help_text='Ingrese un numero de orden', unique=True)),
                ('horaRecepcion', models.TimeField(verbose_name='Hora Recepcion')),
                ('horaEntregaAproximada', models.TimeField(verbose_name='Entrega Aproximada')),
                ('horaEntrega', models.TimeField(blank=True, verbose_name='Entrega')),
                ('facturaAsociada', models.PositiveIntegerField(help_text='Ingrese unicamente numeros positivos', verbose_name='Fact Asociada')),
                ('observaciones', models.TextField(blank=True, max_length=500, verbose_name='Observaciones')),
                ('fechaCreacion', models.DateTimeField(verbose_name='Creada en')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenDeTrabajo.Estado')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicioId', models.AutoField(primary_key=True, serialize=False)),
                ('servicio', models.CharField(max_length=230, verbose_name='Servicio')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('orden', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='ordenDeTrabajo.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('tipoId', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=140)),
                ('orden', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='ordenDeTrabajo.Orden')),
            ],
        ),
        migrations.AddField(
            model_name='detalle',
            name='detalle',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='ordenDeTrabajo.Orden'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='tipoServicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenDeTrabajo.Servicio'),
        ),
    ]