# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-23 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalsetting', '0010_goal_info_balanced_scorecard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal_form',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goal_form',
            name='directorate',
            field=models.CharField(choices=[('CMPMO', 'Change Management and PMO'), ('commercial', 'Commercial Services'), ('cs', 'Corporate Services'), ('fs', 'Financial Services'), ('ict', 'Information Communication and Technology'), ('audit', 'Internal Audit'), ('legal', 'Legal Services and Company Secretariat'), ('risk', 'Risk and Compliance'), ('technical', 'Technical')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goal_form',
            name='supervisor_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goal_form',
            name='unit',
            field=models.CharField(choices=[('change', 'AEDC Change'), ('billing', 'Billing'), ('corp risk', 'Business Corporate Risk'), ('comm perf', 'Commercial Performance Management'), ('comms facilities', 'Communications Facilities and Infrastructure'), ('legal', 'Company Secretariat'), ('comp audit', 'Compliance Audit'), ('contract', 'Contract and Documentation'), ('corp comms', 'Corporate Communications'), ('corp finance', 'Corporate Finance and Corporate Development'), ('ccu', 'Customer Care Services'), ('cyber sec', 'Cyber Security and BCP'), ('dispute', 'Dispute Resolution'), ('Env and social', 'Environmental and Social'), ('fin ops', 'Financial Operations'), ('fleet', 'Fleet Management and Logistics'), ('GIS', 'GIS and Communications'), ('HSE', 'Health and Safety'), ('hr', 'Human Resources and Administration'), ('IT audit', 'IT Audit'), ('key/debt', 'Key/Debt Account'), ('Legal adv', 'Legal Advisory'), ('Legal serv', 'Legal Services'), ('ceo', 'Management Office'), ('Net Dev', 'Network Development'), ('Net Ops', 'Network Operations'), ('ops and maintenance', 'Operations and Maintenance'), ('ops audit', 'Operations Audit'), ('ops control', 'Operations Control'), ('PCC', 'Protetion, Control and Communincations'), ('QA', 'Quality Assurance'), ('rem', 'Real Estate Management'), ('rgr', 'Regulatory and Government Relations'), ('rpu', 'Revenue Protection'), ('ss', 'Security Services'), ('spmo', 'Strategic PMO Office'), ('scp', 'Strategic and Corporate Planning'), ('sc', 'Supply Chain (Procurement)'), ('tfrm', 'Treasury and Financial Risk Management'), ('usam', 'User Support and Application Management'), ('vend', 'Vending')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goal_info',
            name='Balanced_scorecard',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='goal_info',
            name='KPI',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='goal_info',
            name='objective',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='goal_info',
            name='specific_task',
            field=models.TextField(max_length=500),
        ),
    ]
