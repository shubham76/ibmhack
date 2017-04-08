# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0007_auto_20170408_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='item',
            new_name='image_name',
        ),
        migrations.AddField(
            model_name='images',
            name='calorie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='images',
            name='item_name',
            field=models.CharField(default=b'', max_length=40),
        ),
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
