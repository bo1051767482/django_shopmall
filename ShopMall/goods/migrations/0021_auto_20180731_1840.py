# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-31 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0020_auto_20180730_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_evaluate',
            name='evaluate_img',
            field=models.ImageField(blank=True, max_length=200, upload_to='goods', verbose_name='评价图片路径'),
        ),
    ]
