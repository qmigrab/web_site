# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.ImageField(upload_to=b'upload/config/logo/%Y/%M/%D', width_field=b'width', height_field=b'height', blank=True, null=True, verbose_name='LOGO')),
                ('logo_active', models.BooleanField(default=True, verbose_name='Logo Active')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('width', models.PositiveIntegerField(default=0, verbose_name='Width', blank=True)),
                ('height', models.PositiveIntegerField(default=0, verbose_name='Height', blank=True)),
                ('site', models.OneToOneField(related_name='config', to='sites.Site')),
            ],
        ),
    ]
