# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0005_signature_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='optin',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
