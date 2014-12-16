# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0007_remove_signature_signature_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='displayed',
            field=models.BooleanField(default=True, db_index=True),
            preserve_default=True,
        ),
    ]
