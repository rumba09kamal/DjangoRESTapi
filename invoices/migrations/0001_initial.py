# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-13 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
