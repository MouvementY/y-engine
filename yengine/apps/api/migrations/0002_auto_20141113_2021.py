# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='signature_image_data_url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signature',
            name='signature_image',
            field=models.ImageField(upload_to=core.utils.UniqueFilename('petition/signatures/%Y/%m/'), blank=True, null=True),
            preserve_default=True,
        ),
    ]
