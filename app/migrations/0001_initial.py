# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.TextField(max_length=250)),
                ('coordenadasX', models.IntegerField()),
                ('coordenadasY', models.IntegerField()),
            ],
        ),
    ]
