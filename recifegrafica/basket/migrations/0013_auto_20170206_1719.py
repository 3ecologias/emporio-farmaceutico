# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-06 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0012_line_hire_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='hire_art',
            field=models.BooleanField(default=False, verbose_name=b'Contratou servi\xc3\xa7o de arte?'),
        ),
    ]
