# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160418_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.UUIDField(),
        ),
    ]