# Generated by Django 2.0.5 on 2018-05-21 01:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20180520_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designa si el Usuario es o no un miembro activo', verbose_name='Miembro Activo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='las_edit',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_user'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='publicado en'),
        ),
    ]
