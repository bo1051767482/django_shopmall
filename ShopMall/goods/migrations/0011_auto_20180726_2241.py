# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20180726_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods_evaluate',
            old_name='evalute_img',
            new_name='evaluate_img',
        ),
    ]
