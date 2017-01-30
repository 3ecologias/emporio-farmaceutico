# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arts_and_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=b'Artes/', verbose_name=b'Arquivo da arte'),
        ),
        migrations.AlterField(
            model_name='document',
            name='order_number',
            field=models.CharField(max_length=255, null=True, verbose_name=b'N\xc3\xbamero da ordem', blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='product_description',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o do produto', blank=True),
        ),
    ]
