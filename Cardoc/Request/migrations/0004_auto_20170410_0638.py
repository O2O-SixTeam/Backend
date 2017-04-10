# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Request', '0003_auto_20170410_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='broken1',
            field=models.CharField(blank=True, choices=[(1, '범퍼'), ('프론트 판넬', '프론트 판넬'), ('앞 펜더', '앞 펜더'), ('앞 휠하우스', '앞 휠하우스'), ('에이필러', '에이필러'), ('앞문', '앞문'), ('비필러', '비필러'), ('뒷문', '뒷문'), ('뒤 펜더', '뒤 펜더'), ('뒤 휠하우스', '뒤 휠하우스'), ('루프판넬', '루프판넬'), ('트렁크', '트렁크'), ('리어 판넬', '리어 판넬'), ('본네트', '본네트'), ('유리', '유리')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='broken2',
            field=models.CharField(blank=True, choices=[(1, '범퍼'), ('프론트 판넬', '프론트 판넬'), ('앞 펜더', '앞 펜더'), ('앞 휠하우스', '앞 휠하우스'), ('에이필러', '에이필러'), ('앞문', '앞문'), ('비필러', '비필러'), ('뒷문', '뒷문'), ('뒤 펜더', '뒤 펜더'), ('뒤 휠하우스', '뒤 휠하우스'), ('루프판넬', '루프판넬'), ('트렁크', '트렁크'), ('리어 판넬', '리어 판넬'), ('본네트', '본네트'), ('유리', '유리')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='broken3',
            field=models.CharField(blank=True, choices=[(1, '범퍼'), ('프론트 판넬', '프론트 판넬'), ('앞 펜더', '앞 펜더'), ('앞 휠하우스', '앞 휠하우스'), ('에이필러', '에이필러'), ('앞문', '앞문'), ('비필러', '비필러'), ('뒷문', '뒷문'), ('뒤 펜더', '뒤 펜더'), ('뒤 휠하우스', '뒤 휠하우스'), ('루프판넬', '루프판넬'), ('트렁크', '트렁크'), ('리어 판넬', '리어 판넬'), ('본네트', '본네트'), ('유리', '유리')], max_length=10, null=True),
        ),
    ]
