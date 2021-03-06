# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-10 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=1023)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('line_items', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
