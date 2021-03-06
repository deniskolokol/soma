# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-19 14:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.IntegerField(default=1, help_text='Difficulty (on the scale 1..40)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40)])),
                ('asana_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plate_content', to='asana.AsanaForm')),
            ],
        ),
    ]
