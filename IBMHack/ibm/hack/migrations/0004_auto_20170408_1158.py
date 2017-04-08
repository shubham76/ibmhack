# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0003_auto_20170407_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.FileField(upload_to=b'images')),
                ('item', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='activity',
            field=models.IntegerField(),
        ),
    ]
