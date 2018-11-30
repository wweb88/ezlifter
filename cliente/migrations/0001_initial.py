# Generated by Django 2.0.9 on 2018-11-30 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='asensor',
            name='pertenece',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
