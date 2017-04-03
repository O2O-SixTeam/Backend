# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 09:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to=settings.AUTH_USER_MODEL),
        ),
    ]
