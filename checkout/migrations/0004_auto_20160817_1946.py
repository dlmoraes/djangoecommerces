# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20160817_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], max_length=20, verbose_name='Opção de pagamento'),
        ),
    ]
