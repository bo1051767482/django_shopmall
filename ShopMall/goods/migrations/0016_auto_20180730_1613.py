# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-30 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0015_auto_20180730_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goods.goods_type', verbose_name='分类ID'),
        ),
    ]
