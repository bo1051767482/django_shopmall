# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_auto_20180726_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_evaluate',
            name='evalute_img',
            field=models.ImageField(max_length=200, upload_to='goods', verbose_name='评价图片路径'),
        ),
    ]
