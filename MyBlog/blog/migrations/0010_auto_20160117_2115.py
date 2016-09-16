# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='numbers_of_articles',
        ),
        migrations.AddField(
            model_name='article',
            name='name_of_subject',
            field=models.ForeignKey(to='blog.Subject', null=True),
        ),
    ]
