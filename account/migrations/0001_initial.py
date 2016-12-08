# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, db_index=True, default=b'', max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_per_page', models.IntegerField(default=25, verbose_name='Items per page')),
                ('password_changed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
