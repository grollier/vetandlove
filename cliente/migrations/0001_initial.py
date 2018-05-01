# Generated by Django 2.0.4 on 2018-04-30 07:06

import django.core.validators
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
                ('password', models.CharField(default='132435', max_length=12)),
                ('fechaNacimiento', models.DateField()),
                ('fechaCreacion', models.DateTimeField(auto_now=True, verbose_name='publicado_en')),
            ],
        ),
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('correoId', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=100, validators=[django.core.validators.EmailValidator(message='Correo Invalido')])),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccionId', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=240)),
                ('colonia', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('municipioId', models.AutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('telefonoId', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=8, unique=True)),
                ('tipodeTelefono', models.CharField(choices=[('celular', 'CELULAR'), ('trabajo', 'TRABAJO'), ('casa', 'CASA'), ('otro', 'OTRO')], default='CELULAR', max_length=7)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('zonaId', models.AutoField(primary_key=True, serialize=False)),
                ('zona', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='municipio',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='cliente.Municipio'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='zona',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='cliente.Zona'),
        ),
    ]
