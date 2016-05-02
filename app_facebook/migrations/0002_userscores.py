# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-30 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='puntaje')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facebook.User')),
            ],
            options={
                'db_table': 'app_facebook_user_score',
            },
        ),
    ]