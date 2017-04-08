# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0005_auto_20170408_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.FileField(upload_to=b'/static/images1'),
        ),
    ]
