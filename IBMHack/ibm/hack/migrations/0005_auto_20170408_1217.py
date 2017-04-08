# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0004_auto_20170408_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.FileField(upload_to=b'images1'),
        ),
    ]
