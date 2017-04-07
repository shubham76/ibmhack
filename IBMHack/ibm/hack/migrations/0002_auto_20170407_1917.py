# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='lname',
        ),
    ]
