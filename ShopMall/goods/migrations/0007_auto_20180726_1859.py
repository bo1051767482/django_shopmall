# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_goods_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_evaluate',
            name='goods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='goods_evaluate',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.member', verbose_name='用户ID'),
        ),
    ]
