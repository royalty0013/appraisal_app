# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-26 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalsetting', '0012_goal_form_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal_form',
            name='total',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
