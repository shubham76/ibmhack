# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0008_auto_20170408_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date'),
        ),
    ]
