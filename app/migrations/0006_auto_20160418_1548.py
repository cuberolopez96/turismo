# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160418_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidadautonoma',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]
