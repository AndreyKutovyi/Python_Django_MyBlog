# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_subject_numbers_of_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='numbers_of_articles',
            field=models.ManyToManyField(to='blog.Article'),
        ),
    ]
