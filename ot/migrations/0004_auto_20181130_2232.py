# Generated by Django 2.0.9 on 2018-12-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot', '0003_auto_20181130_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_tecnico',
            name='hora_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente_tecnico',
            name='hora_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]
