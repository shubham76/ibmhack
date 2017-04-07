# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0002_auto_20170407_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='activity',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='tee',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
