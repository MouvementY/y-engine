# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='signature',
            table=None,
        ),
        migrations.RunSQL("ALTER SEQUENCE api_signature_id_seq RENAME TO bill_signature_id_seq;"),
        migrations.RunSQL("ALTER INDEX api_signature_pkey RENAME TO bill_signature_pkey;"),
    ]
