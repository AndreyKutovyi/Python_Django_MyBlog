# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_subject_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Kyiv', null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subjects',
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(to='blog.Subject'),
        ),
    ]
