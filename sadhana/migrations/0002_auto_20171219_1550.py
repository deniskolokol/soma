# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-19 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sadhana', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plate',
            name='asana_form',
        ),
        migrations.DeleteModel(
            name='Plate',
        ),
    ]
