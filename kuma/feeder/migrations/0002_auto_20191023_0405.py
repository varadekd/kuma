# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-23 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='shortname',
            field=models.SlugField(help_text='Short name to find this bundle by.', unique=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='keep',
            field=models.PositiveIntegerField(default=0, help_text='Discard all but this amount of entries. 0 == do not discard.'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='shortname',
            field=models.SlugField(help_text='Short name to find this feed by.', unique=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Modified'),
        ),
    ]
