# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitationelementdata',
            name='count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
