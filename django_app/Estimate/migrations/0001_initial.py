# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noninsurancecost', models.CharField(blank=True, max_length=20, null=True)),
                ('insurancecost', models.CharField(blank=True, max_length=20, null=True)),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
                ('completed', models.NullBooleanField()),
            ],
        ),
    ]
