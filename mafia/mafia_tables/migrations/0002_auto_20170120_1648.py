# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mafia_tables', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='result',
        ),
        migrations.AddField(
            model_name='tasks',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='personhastasks',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
