# Generated by Django 3.1 on 2021-02-06 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_auto_20210206_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='avatar',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postImage',
            field=models.URLField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postText',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postTimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 12, 3, 48, 659658), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=50000),
        ),
    ]
