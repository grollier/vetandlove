# Generated by Django 2.0.5 on 2018-06-25 00:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('clienteId', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electronico')),
                ('is_active', models.BooleanField(default=True, help_text='Designa si el Usuario es o no un miembro activo', verbose_name='Miembro Activo')),
                ('password', models.CharField(default=132435, max_length=12)),
                ('fechaNacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, null=True, verbose_name='publicado en')),
                ('las_edit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_user')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccionId', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=240)),
                ('colonia', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='cliente.Cliente')),
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
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='cliente.Zona'),
        ),
    ]
