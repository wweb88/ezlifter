# Generated by Django 2.0.9 on 2018-11-30 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0006_auto_20181130_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente_Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.DateTimeField()),
                ('hora_termino', models.DateTimeField()),
                ('fallas', models.CharField(max_length=255)),
                ('piezas', models.CharField(max_length=255)),
                ('encargado', models.CharField(max_length=100)),
                ('id_ascensor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Ascensor')),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
