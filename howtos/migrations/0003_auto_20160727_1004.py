# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtos', '0002_entry_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
