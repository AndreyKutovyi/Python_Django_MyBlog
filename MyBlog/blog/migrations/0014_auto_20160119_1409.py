# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160119_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='photo',
            new_name='image',
        ),
    ]
