# Generated by Django 2.0.4 on 2018-04-15 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('clienteId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dpi', models.CharField(max_length=13, unique=True, verbose_name='DPI')),
                ('fechaNacimiento', models.DateField()),
                ('fechaCreacion', models.DateTimeField(auto_now=True, verbose_name='publicado en')),
            ],
        ),
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('correoId', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=100)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('telefonoId', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=8)),
                ('tipodTelefono', models.CharField(choices=[('celular', 'CELULAR'), ('trabajo', 'TRABAJO'), ('casa', 'CASA'), ('otro', 'OTRO')], default='CELULAR', max_length=7)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
    ]