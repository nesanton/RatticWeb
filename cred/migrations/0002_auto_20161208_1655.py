# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cred', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('tag', models.ForeignKey(to='cred.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(db_index=True, max_length=250, null=True, blank=True)),
                ('extra', models.ForeignKey(to='cred.Extra')),
            ],
        ),
        migrations.AlterField(
            model_name='credaudit',
            name='audittype',
            field=models.CharField(max_length=1, choices=[(b'A', 'Added'), (b'C', 'Changed'), (b'M', 'Only Metadata Changed'), (b'V', 'Only Details Viewed'), (b'X', 'Exported'), (b'D', 'Deleted'), (b'S', 'Scheduled For Change'), (b'P', 'Password Viewed'), (b'E', 'Extra Fields Changed')]),
        ),
        migrations.AddField(
            model_name='cred',
            name='extrafields',
            field=models.ManyToManyField(default=None, to='cred.ExtraField', null=True, blank=True),
        ),
    ]
