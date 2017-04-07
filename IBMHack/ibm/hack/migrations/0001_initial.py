# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('unique_id', models.IntegerField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('weight', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=10)),
                ('activity', models.CharField(max_length=20)),
                ('tee', models.IntegerField(default=0)),
            ],
        ),
    ]
