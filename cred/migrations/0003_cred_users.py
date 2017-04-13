# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cred', '0002_auto_20161208_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='cred',
            name='users',
            field=models.ManyToManyField(related_name='child_creds', default=None, to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Users'),
        ),
    ]
