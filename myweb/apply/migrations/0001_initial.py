# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Applicant')),
                ('email', models.EmailField(max_length=60, verbose_name='Email')),
                ('content', models.TextField(verbose_name='Content')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='Send')),
            ],
        ),
    ]
