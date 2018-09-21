# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 01:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_companyadminmodel'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='companyadminmodel',
            unique_together=set([('user', 'company')]),
        ),
    ]
