# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-28 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='user_name',
            field=models.CharField(max_length=300),
        ),
    ]