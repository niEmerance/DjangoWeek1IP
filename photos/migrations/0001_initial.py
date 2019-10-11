# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgName', models.CharField(max_length=30)),
                ('imgDesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgCategory', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locName', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='imgCtgry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.ImageCategory'),
        ),
        migrations.AddField(
            model_name='image',
            name='imgLoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.ImageLocation'),
        ),
    ]
