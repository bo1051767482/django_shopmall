# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-31 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0021_auto_20180731_1840'),
        ('home', '0007_auto_20180729_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopping_car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='数量')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('goods', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品ID')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.member', verbose_name='用户名')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车商品信息',
            },
        ),
    ]
