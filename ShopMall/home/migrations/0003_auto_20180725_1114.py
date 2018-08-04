# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-25 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180724_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='member',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='账户创建时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(default=0, max_length=40, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_login_time',
            field=models.DateTimeField(verbose_name='最后一次登录时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(max_length=30, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=32, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default=0, max_length=11, unique=True, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='member',
            name='qq',
            field=models.CharField(default=0, max_length=20, verbose_name='QQ'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.IntegerField(choices=[(0, '不设置'), (1, '男'), (2, '女')], default=0, verbose_name='性别'),
        ),
    ]
