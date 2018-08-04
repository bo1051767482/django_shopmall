# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 10:20
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='商品名名称')),
                ('title', models.CharField(max_length=150, verbose_name='商品说明')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('promotion_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='促销价')),
                ('type_id', models.ForeignKey('goods_type',default=1,verbose_name='分类ID')),
                ('disabled', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('stoc', models.IntegerField(default=0, verbose_name='库存')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='goods_evaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0, verbose_name='用户ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评价时间')),
                ('goods_id', models.IntegerField(default=0, verbose_name='商品ID')),
                ('evaluate_content', models.TextField(verbose_name='评价内容')),
                ('evalute_img', models.TextField(verbose_name='评价图片')),
                ('evaluate_type', models.IntegerField(default=5, verbose_name='评价星级')),
            ],
            options={
                'verbose_name': '商品评价',
                'verbose_name_plural': '商品评价信息',
            },
        ),
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
        migrations.CreateModel(
            name='goods_introduces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', max_length=10240000000000000, verbose_name='商品介绍')),
                ('afte_sale', DjangoUeditor.models.UEditorField(blank=True, default='', max_length=10240000000000000, verbose_name='售后')),
                ('goods', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
            ],
            options={
                'verbose_name': '商品介绍',
                'verbose_name_plural': '商品详细信息',
            },
        ),
    ]
