# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0006_auto_20170408_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='img',
        ),
        migrations.AddField(
            model_name='images',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
