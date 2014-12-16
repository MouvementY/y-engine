# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0006_signature_optin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signature',
            name='signature_image',
        ),
    ]
