# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-03 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ElementData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('threat_one', models.FloatField(default=0)),
                ('threat_two', models.FloatField(default=0)),
                ('threat_three', models.FloatField(default=0)),
                ('threat_four', models.FloatField(default=0)),
                ('threat_five', models.FloatField(default=0)),
                ('hazards', models.CharField(blank=True, max_length=255, null=True)),
                ('remedy', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HabitationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HabitationElementData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('as_actual', models.FloatField(default=0)),
                ('fe_actual', models.FloatField(default=0)),
                ('f_actual', models.FloatField(default=0)),
                ('salinity_actual', models.FloatField(default=0)),
                ('nitrate_actual', models.FloatField(default=0)),
                ('as_bis', models.FloatField(default=0)),
                ('fe_bis', models.FloatField(default=0)),
                ('f_bis', models.FloatField(default=0)),
                ('salinity_bis', models.FloatField(default=0)),
                ('nitrate_bis', models.FloatField(default=0)),
                ('created', models.CharField(max_length=255)),
                ('habitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.HabitationData')),
            ],
        ),
        migrations.CreateModel(
            name='PanchayatData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.BlockData')),
            ],
        ),
        migrations.CreateModel(
            name='StateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VillageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('panchayat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.PanchayatData')),
            ],
        ),
        migrations.AddField(
            model_name='habitationdata',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.VillageData'),
        ),
        migrations.AddField(
            model_name='districtdata',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.StateData'),
        ),
        migrations.AddField(
            model_name='blockdata',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.DistrictData'),
        ),
    ]
