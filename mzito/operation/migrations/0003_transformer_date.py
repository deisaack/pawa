# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_transformer_power_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformer',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Installation date '),
        ),
    ]