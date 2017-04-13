# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.10.6 on 2017-04-11 12:42
=======
# Generated by Django 1.10.6 on 2017-04-13 07:25
>>>>>>> master
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=20, null=True)),
                ('model', models.CharField(blank=True, max_length=20, null=True)),
                ('carnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('broken1', models.CharField(blank=True, choices=[('범퍼', '범퍼'), ('프론트 판넬', '프론트 판넬'), ('앞 펜더', '앞 펜더'), ('앞 휠하우스', '앞 휠하우스'), ('에이필러', '에이필러'), ('앞문', '앞문'), ('비필러', '비필러'), ('뒷문', '뒷문'), ('뒤 펜더', '뒤 펜더'), ('뒤 휠하우스', '뒤 휠하우스'), ('루프판넬', '루프판넬'), ('트렁크', '트렁크'), ('리어 판넬', '리어 판넬'), ('본네트', '본네트'), ('유리', '유리')], max_length=10, null=True)),
                ('broken2', models.CharField(blank=True, choices=[('범퍼', '범퍼'), ('프론트 판넬', '프론트 판넬'), ('앞 펜더', '앞 펜더'), ('앞 휠하우스', '앞 휠하우스'), ('에이필러', '에이필러'), ('앞문', '앞문'), ('비필러', '비필러'), ('뒷문', '뒷문'), ('뒤 펜더', '뒤 펜더'), ('뒤 휠하우스', '뒤 휠하우스'), ('루프판넬', '루프판넬'), ('트렁크', '트렁크'), ('리어 판넬', '리어 판넬'), ('본네트', '본네트'), ('유리', '유리')], max_length=10, null=True)),
                ('broken3', models.CharField(blank=True, choices=[('범퍼', '범퍼'), ('프론트 판넬', '프론트 판넬'), ('앞 펜더', '앞 펜더'), ('앞 휠하우스', '앞 휠하우스'), ('에이필러', '에이필러'), ('앞문', '앞문'), ('비필러', '비필러'), ('뒷문', '뒷문'), ('뒤 펜더', '뒤 펜더'), ('뒤 휠하우스', '뒤 휠하우스'), ('루프판넬', '루프판넬'), ('트렁크', '트렁크'), ('리어 판넬', '리어 판넬'), ('본네트', '본네트'), ('유리', '유리')], max_length=10, null=True)),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='')),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
                ('extra', models.CharField(blank=True, choices=[('보험수리', '보험수리'), ('렌터카', '렌터카'), ('픽업 서비스', '픽업 서비스'), ('차대번호', '차대번호')], max_length=10, null=True)),
                ('number', models.CharField(blank=True, max_length=11, null=True)),
                ('completed', models.NullBooleanField()),
            ],
        ),
    ]
