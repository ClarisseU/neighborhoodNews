# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-03 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='business',
            name='buzz_email',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
