# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151207_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
    ]
