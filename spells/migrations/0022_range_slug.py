# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0021_auto_20160922_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', editable=False, max_length=100),
            preserve_default=False,
        ),
    ]