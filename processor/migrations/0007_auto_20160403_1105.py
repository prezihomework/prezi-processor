# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0006_auto_20160403_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
