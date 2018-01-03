# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_score_scoreditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreditem',
            name='created',
        ),
        migrations.RemoveField(
            model_name='scoreditem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='scoreditem',
            name='note',
        ),
        migrations.RemoveField(
            model_name='scoreditem',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='scoreditem',
            name='user',
        ),
        migrations.AddField(
            model_name='scoreditem',
            name='val',
            field=models.PositiveIntegerField(default=0),
        ),
    ]