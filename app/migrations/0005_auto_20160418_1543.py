# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160418_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidadautonoma',
            name='nombre',
            field=models.UUIDField(),
        ),
    ]
