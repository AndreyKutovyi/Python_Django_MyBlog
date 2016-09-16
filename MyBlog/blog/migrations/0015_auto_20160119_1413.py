# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160119_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(help_text=b'150x150px', upload_to=b'images/', null=True, verbose_name='\u0412\u0430\u0448\u0435 \u0444\u043e\u0442\u043e'),
        ),
    ]
