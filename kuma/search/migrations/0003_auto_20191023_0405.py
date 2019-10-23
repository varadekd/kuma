# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-23 04:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20191002_filter_base_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='default',
            field=models.BooleanField(default=False, help_text='Whether this filter is applied in the absence of a user-chosen filter'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='enabled',
            field=models.BooleanField(default=True, help_text='Whether this filter is shown to users or not.'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='group',
            field=models.ForeignKey(help_text='E.g. "Topic", "Skill level" etc', on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='search.FilterGroup'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='name',
            field=models.CharField(db_index=True, help_text='the English name of the filter to be shown in the frontend UI', max_length=255),
        ),
        migrations.AlterField(
            model_name='filter',
            name='operator',
            field=models.CharField(choices=[('OR', 'OR'), ('AND', 'AND')], default='OR', help_text='The logical operator to use if more than one tag is given', max_length=3),
        ),
        migrations.AlterField(
            model_name='filter',
            name='shortcut',
            field=models.CharField(blank=True, db_index=True, help_text='the name of the shortcut to show in the command and query UI. e.g. fxos', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='slug',
            field=models.CharField(db_index=True, help_text='the slug to be used as a query parameter in the search URL', max_length=255),
        ),
        migrations.AlterField(
            model_name='filter',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags. If more than one tag given the operator specified is used', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='visible',
            field=models.BooleanField(default=True, help_text='Whether this filter is shown at public places, e.g. the command and query UI'),
        ),
        migrations.AlterField(
            model_name='filtergroup',
            name='order',
            field=models.IntegerField(default=1, help_text='An integer defining which order the filter group should show up in the sidebar'),
        ),
        migrations.AlterField(
            model_name='filtergroup',
            name='slug',
            field=models.CharField(blank=True, help_text='the slug to be used as the name of the query parameter in the search URL', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='name',
            field=models.CharField(blank=True, help_text='The search index name, set to the created date when left empty', max_length=30, null=True),
        ),
    ]
