# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 10:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='goods_introduces',
            new_name='goods_introduce',
        ),
    ]
