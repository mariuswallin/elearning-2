# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20190519_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventguest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Host'), (1, 'Guest'), (2, 'Desisted'), (3, 'Confirmed')]),
        ),
    ]
