# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20180726_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(max_length=200, upload_to='goods', verbose_name='图片路径')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('goods', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品内容图片',
            },
        ),
    ]
