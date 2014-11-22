# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(verbose_name='Prénom', max_length=150)),
                ('last_name', models.CharField(verbose_name='Nom', max_length=150)),
                ('email', models.EmailField(verbose_name='Email', max_length=75, unique=True)),
                ('signature_image', models.ImageField(blank=True, null=True, upload_to=core.utils.UniqueFilename('petition/signatures/%Y/%m/'))),
                ('signature_image_data_url', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
