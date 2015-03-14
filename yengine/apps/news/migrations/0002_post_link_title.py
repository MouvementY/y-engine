# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link_title',
            field=models.CharField(verbose_name='Titre du lien', null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
