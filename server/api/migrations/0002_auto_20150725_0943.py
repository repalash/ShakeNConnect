# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='fingerprint',
            field=models.TextField(unique=True),
            preserve_default=True,
        ),
    ]
