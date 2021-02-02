# Generated by Django 3.1 on 2021-01-31 19:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20210131_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postTimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 1, 18, 22, 590459)),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follwer', to='twitter.user')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.user')),
            ],
        ),
    ]