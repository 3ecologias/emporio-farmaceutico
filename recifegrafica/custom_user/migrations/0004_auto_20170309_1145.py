# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-09 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20170215_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
    ]
