# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141113_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='email',
            field=models.EmailField(max_length=75, unique=True, verbose_name='Email'),
            preserve_default=True,
        ),
    ]
