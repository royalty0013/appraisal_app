# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0003_auto_20191127_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accomplishment',
            old_name='business_impact',
            new_name='balanced_scorecard',
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='strategic_focus',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='appraisal_info',
            name='appraiser_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appraisal_info',
            name='average',
            field=models.IntegerField(default=0),
        ),
    ]
