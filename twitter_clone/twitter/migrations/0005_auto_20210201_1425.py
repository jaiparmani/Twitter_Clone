# Generated by Django 3.1 on 2021-02-01 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20210201_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='commentText',
        ),
        migrations.AlterField(
            model_name='posts',
            name='postTimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 14, 25, 17, 488705)),
        ),
    ]