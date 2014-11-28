# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='banned',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
