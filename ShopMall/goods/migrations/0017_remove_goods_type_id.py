# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-30 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0016_auto_20180730_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='type_id',
        ),
    ]
