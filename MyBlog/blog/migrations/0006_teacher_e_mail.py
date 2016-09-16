# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151207_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='e_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
