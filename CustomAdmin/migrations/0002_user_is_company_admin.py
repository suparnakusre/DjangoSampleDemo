# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_company_admin',
            field=models.BooleanField(default=False),
        ),
    ]