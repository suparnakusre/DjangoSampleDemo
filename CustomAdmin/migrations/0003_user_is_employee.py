# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAdmin', '0002_user_is_company_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
