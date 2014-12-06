# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0004_auto_20141205_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
