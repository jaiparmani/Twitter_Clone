# Generated by Django 3.1 on 2021-01-31 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20210129_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postTimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 21, 28, 5, 197147)),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='imgs'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
