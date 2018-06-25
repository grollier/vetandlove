# Generated by Django 2.0.5 on 2018-06-25 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('especieId', models.AutoField(primary_key=True, serialize=False)),
                ('tipoEspecie', models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otros')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Kennel',
            fields=[
                ('kennelId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_kennel', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('mascotaId', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMascota', models.CharField(max_length=50, verbose_name='Nombre')),
                ('observaciones', models.TextField(blank=True, max_length=240, null=True)),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Peso')),
                ('altura', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Altura')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, verbose_name='publicado en')),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascota.Especie')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('razaId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_raza', models.CharField(max_length=128)),
                ('origen', models.CharField(max_length=130)),
                ('especie_raza', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='especies', to='mascota.Especie')),
                ('kennel', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='kennels', to='mascota.Kennel')),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='mascota.Raza'),
        ),
        migrations.AddField(
            model_name='kennel',
            name='kennel',
            field=models.ManyToManyField(through='mascota.Raza', to='mascota.Especie'),
        ),
    ]
