# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], default='credit', max_length=6)),
                ('transaction_value', models.PositiveIntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProofOfTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='cashflow',
            name='transaction_proof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cash.ProofOfTransaction'),
        ),
    ]
