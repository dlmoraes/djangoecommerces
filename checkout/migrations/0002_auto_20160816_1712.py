# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-16 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set([('cart_key', 'product')]),
        ),
    ]
