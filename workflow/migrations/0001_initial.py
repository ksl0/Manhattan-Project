# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('photo_assignment', 'Photo Assignment'), ('article_assignment', 'Article Assignment')], max_length=50, default='photo_assignment')),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignmentForm',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('position', models.CharField(choices=[('chief_editor', 'Chief Editor'), ('copy_editor', 'Copy Editor'), ('photographer', 'Photographer'), ('author', 'Author'), ('graphic_designer', 'Graphic Designer'), ('web_developer', 'Web Developer')], max_length=50, default='Editor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reviewer', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('article', models.ForeignKey(to='mainsite.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('editor', models.ForeignKey(to='workflow.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField()),
                ('article', models.OneToOneField(to='mainsite.Article')),
                ('locker', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assignment',
            name='receiver',
            field=models.ForeignKey(to='workflow.Profile', related_name='assignment_received', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_article',
            field=models.ForeignKey(null=True, related_name='assignment', to='mainsite.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_photo',
            field=models.ForeignKey(null=True, related_name='assignment', to='mainsite.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.ForeignKey(to='mainsite.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='sender',
            field=models.ForeignKey(to='workflow.Profile', related_name='assignment_created'),
            preserve_default=True,
        ),
    ]
