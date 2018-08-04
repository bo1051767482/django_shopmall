# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-30 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0014_auto_20180728_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='类别名')),
                ('parent_id', models.IntegerField(default=0, verbose_name='父类ID')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类表表',
            },
        ),
        migrations.AlterModelOptions(
            name='goods_tj',
            options={'verbose_name': '商品推荐', 'verbose_name_plural': '商品推荐表'},
        ),
    ]
