# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
