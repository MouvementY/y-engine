# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141120_0328'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signature',
        ),
    ]
