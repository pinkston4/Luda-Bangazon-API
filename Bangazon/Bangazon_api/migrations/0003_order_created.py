# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bangazon_api', '0002_auto_20170125_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]