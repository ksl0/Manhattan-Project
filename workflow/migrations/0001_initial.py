# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(default='photo_assignment', choices=[('photo', 'Photo Assignment'), ('article', 'Article Assignment')], max_length=50)),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('position', models.CharField(default='Editor', choices=[('chief_editor', 'Chief Editor'), ('copy_editor', 'Copy Editor'), ('photographer', 'Photographer'), ('author', 'Author'), ('graphic_designer', 'Graphic Designer'), ('web_developer', 'Web Developer')], max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
            field=models.ForeignKey(related_name='assignment_received', null=True, to='workflow.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_article',
            field=models.ForeignKey(related_name='assignment', null=True, to='mainsite.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_photo',
            field=models.ForeignKey(related_name='assignment', null=True, to='mainsite.Photo'),
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
