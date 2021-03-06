# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Request', '0001_initial'),
        ('Estimate', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estimate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estimate',
            name='targetrequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Request.Request'),
        ),
    ]
