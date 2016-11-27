# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], default='credit', max_length=5),
        ),
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='value',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
    ]
