# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-06 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import recifegrafica.order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20170203_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='art_file',
            field=models.FileField(blank=True, null=True, upload_to=recifegrafica.order.models.user_directory_path, verbose_name=b'Arquivo da arte'),
        ),
    ]
