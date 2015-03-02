# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('title', models.CharField(verbose_name='Titre', max_length=150)),
                ('text', models.TextField(verbose_name='Texte', blank=True, null=True)),
                ('link', models.URLField(verbose_name='Lien', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
