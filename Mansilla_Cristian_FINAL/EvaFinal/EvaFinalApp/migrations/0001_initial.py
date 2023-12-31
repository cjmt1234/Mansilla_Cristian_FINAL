# Generated by Django 4.2.4 on 2023-12-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=12)),
                ('fechaInscripcion', models.DateField()),
                ('institucion', models.CharField(max_length=80)),
                ('hora', models.TimeField()),
                ('estado', models.CharField(max_length=60)),
                ('observacion', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
    ]
