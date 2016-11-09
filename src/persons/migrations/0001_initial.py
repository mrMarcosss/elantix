# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 17:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Allowed format: '+000000000'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
