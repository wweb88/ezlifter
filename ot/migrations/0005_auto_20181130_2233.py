# Generated by Django 2.0.9 on 2018-12-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot', '0004_auto_20181130_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_tecnico',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente_tecnico',
            name='hora_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente_tecnico',
            name='hora_termino',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
