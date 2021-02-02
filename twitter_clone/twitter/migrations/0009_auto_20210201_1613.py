# Generated by Django 3.1 on 2021-02-01 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0008_auto_20210201_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='imgs'),
        ),
        migrations.AddField(
            model_name='posts',
            name='displayName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='posts',
            name='verified',
            field=models.BooleanField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='postImage',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postTimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 16, 13, 5, 826110)),
        ),
    ]
