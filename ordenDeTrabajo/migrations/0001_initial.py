# Generated by Django 2.0.5 on 2018-06-21 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estados', models.CharField(choices=[('N', 'Nueva'), ('A', 'Activa'), ('F', 'Finalizada'), ('C', 'Cancelada')], help_text='Estado de la Orden', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('ordenId', models.AutoField(primary_key=True, serialize=False)),
                ('nombreOrden', models.CharField(default='Orden de Compra', max_length=16)),
                ('horaRecepcion', models.TimeField(verbose_name='Hora_Recepcion')),
                ('horaEntregaAproximada', models.TimeField(verbose_name='Entrega_Aproximada')),
                ('horaEntrega', models.TimeField(verbose_name='Entrega')),
                ('facturaAsociada', models.CharField(blank=True, max_length=240, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observaciones')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, verbose_name='Creada_en')),
                ('estado_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenDeTrabajo.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicioId', models.AutoField(primary_key=True, serialize=False)),
                ('servicios', models.CharField(choices=[('Consulta', (('CONSULTA', 'Consulta General'), ('EMERGENCIA', 'Consulta de Emergencia'), ('DESPARASITACION', 'Desparasitacion'), ('VACUNAP', 'Vacunas Perro'), ('VACUNAD', 'Vacuna + Desparasitacion'), ('VACUNAG', 'Vacunas Gatos'), ('INYECCION', 'Inyeccion en consulta'), ('LIMPIEZA', 'Limpieza Denta'), ('OTOHEMATOMA', 'Otohematoma'), ('OVHELECTIVA', 'OVH electiva'), ('PIOMETRA', 'Piometra'), ('ORQUIECTOMIA', 'Orquiectomia'), ('EUTANASIA', 'Eutanasia'))), ('Prueba', (('HEMATOLOGIA', 'Hematologia'), ('BILIRRUBINA', 'Bilirrubinas'), ('BILIRRUBINAD', 'Bilirrubina Directa'), ('BILIRRUBINAI', 'Bilirrubina Indirecta'), ('CALCIO', 'Calcio'), ('COLESTEROLT', 'Colesterol Total'), ('CREATININA', 'Creatinina'), ('FOSFATAA', 'Fosfata Alcalina'), ('GLUCOSA', 'Glucosa'), ('NITROGENOU', 'Nitrogeno de Urea'), ('PROTEINAST', 'Proteinas Totales'), ('TGP/ALAT', 'TGP/ALAT'), ('TGO/ASAT', 'TGO/ASAT'), ('TRIGLICERIDOS', 'Trigliceridos'), ('UREA', 'Urea'), ('FIBRINOGENO', 'Fibrinogeno'), ('TPROTOMBINA', 'Tiempo de Protombina'), ('TTROMBOPLASTINAT', 'Tiempo de Tromboplastina'), ('T4LIBRE', 'T4 Libre'), ('ORINA', 'Orina')))], help_text='Elija un servicio para la mascota', max_length=20)),
                ('precio_servicio', models.DecimalField(blank=True, decimal_places=2, help_text='Ingrese el precio del servicio', max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='servicio_orden',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_de_orden', to='ordenDeTrabajo.Servicio'),
        ),
    ]
