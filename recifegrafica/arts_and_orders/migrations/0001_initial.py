# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.CharField(max_length=255, verbose_name=b'N\xc3\xbamero da ordem', blank=True)),
                ('document', models.FileField(upload_to=b'documents/', verbose_name=b'Arquivo da arte')),
                ('product_description', models.CharField(max_length=500, verbose_name=b'Descri\xc3\xa7\xc3\xa3o do produto', blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
