# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blacklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist',
            name='readonly',
            field=models.BooleanField(verbose_name='Readonly authorize', default=True),
            preserve_default=True,
        ),
    ]
