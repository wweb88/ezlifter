# Generated by Django 2.0.9 on 2018-11-30 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_cliente_tecnico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente_tecnico',
            name='id_ascensor',
        ),
        migrations.RemoveField(
            model_name='cliente_tecnico',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='cliente_tecnico',
            name='id_usuario',
        ),
        migrations.DeleteModel(
            name='Cliente_Tecnico',
        ),
    ]
