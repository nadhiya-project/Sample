# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-06-05 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profilepic'),
        ),
    ]
