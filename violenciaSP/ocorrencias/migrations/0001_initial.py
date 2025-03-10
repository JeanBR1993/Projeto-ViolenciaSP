# Generated by Django 5.1.6 on 2025-02-08 00:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delegacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereço', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(validators=[django.core.validators.MinValueValidator(2001), django.core.validators.MaxValueValidator(2100)])),
                ('mes', models.CharField(choices=[('Jan', 'Janeiro'), ('Fev', 'Feveireiro'), ('Mar', 'Março'), ('Abr', 'Abril'), ('Mai', 'Maio'), ('Jun', 'Junho'), ('Jul', 'Julho'), ('Ago', 'Agosto'), ('Set', 'Setembro'), ('Out', 'Outubro'), ('Nov', 'Novembro'), ('Dez', 'Dezembro')], max_length=3)),
                ('nCrimes', models.PositiveIntegerField()),
                ('crime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ocorrencias.crime')),
                ('delegacia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ocorrencias.delegacia')),
            ],
        ),
    ]
