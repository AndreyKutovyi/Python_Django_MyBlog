# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_teacher_e_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='numbers_of_articles',
            field=models.ManyToManyField(to='blog.Article', null=True),
        ),
    ]
