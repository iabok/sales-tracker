# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20170717_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='station',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
