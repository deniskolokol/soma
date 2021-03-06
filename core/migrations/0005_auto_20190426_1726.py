# Generated by Django 2.2 on 2019-04-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190426_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Created'),
        ),
        migrations.AlterField(
            model_name='score',
            name='name',
            field=models.CharField(db_index=True, help_text='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='score',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Last updated'),
        ),
        migrations.AlterField(
            model_name='scoreditem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Created'),
        ),
        migrations.AlterField(
            model_name='scoreditem',
            name='name',
            field=models.CharField(db_index=True, help_text='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='scoreditem',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Last updated'),
        ),
        migrations.AlterField(
            model_name='taggeduseritem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Created'),
        ),
        migrations.AlterField(
            model_name='taggeduseritem',
            name='name',
            field=models.CharField(db_index=True, help_text='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='taggeduseritem',
            name='updated',
            field=models.DateTimeField(auto_now=True, help_text='Last updated'),
        ),
    ]
