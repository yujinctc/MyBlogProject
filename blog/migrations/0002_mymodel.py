# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfield', markdownx.models.MarkdownxField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]