# Generated by Django 3.1 on 2021-01-29 12:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.CharField(max_length=200)),
                ('commentLikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('displayName', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('avatar', models.FileField(upload_to='')),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('postID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('postImage', models.FileField(upload_to='')),
                ('postLikes', models.IntegerField()),
                ('postTimestamp', models.DateTimeField(default=datetime.datetime(2021, 1, 29, 18, 28, 34, 85993))),
                ('postText', models.CharField(max_length=500)),
                ('commentText', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.postcomments')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.user')),
            ],
        ),
        migrations.AddField(
            model_name='postcomments',
            name='postID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.posts'),
        ),
        migrations.AddField(
            model_name='postcomments',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.user'),
        ),
    ]
