# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asana', '0002_auto_20171220_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asanaform',
            name='pict',
            field=models.ImageField(height_field='pict_height', help_text='Pictogram 100x100px', max_length=255, upload_to='asana/pict/', width_field='pict_width'),
        ),
    ]