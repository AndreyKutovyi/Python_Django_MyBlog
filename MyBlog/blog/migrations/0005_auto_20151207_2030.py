# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151207_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.IntegerField(null=True, verbose_name='\u041a\u0443\u0440\u0441 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0447\u0438\u0442\u0430\u0435\u0442\u044c\u0441\u044f \u043f\u0440\u0435\u0434\u043c\u0435\u0442'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='midle_name',
            field=models.CharField(max_length=50, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subjects',
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ForeignKey(to='blog.Subject', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
    ]
