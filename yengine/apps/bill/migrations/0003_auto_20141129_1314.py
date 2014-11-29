# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_signature_banned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='signature_image_data_url',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
