# Generated by Django 2.2 on 2019-04-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asana', '0003_auto_20171220_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asana',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Created', null=True),
        ),
        migrations.AlterField(
            model_name='asana',
            name='name',
            field=models.CharField(db_index=True, default='', help_text='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='asana',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Last updated', null=True),
        ),
    ]
