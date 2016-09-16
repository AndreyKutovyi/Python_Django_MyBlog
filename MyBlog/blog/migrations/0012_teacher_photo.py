# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'images/photo_of_teacher/'),
        ),
    ]
