# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_auto_20141129_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='date_created',
            field=models.DateTimeField(db_index=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
