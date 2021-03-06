# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import pets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=' ', max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(default=' ', max_length=50, verbose_name='Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50, verbose_name='Name')),
                ('type', models.CharField(choices=[('Dog', 'Dog'), ('Parrot', 'Parrot'), ('Rabbit', 'Rabbit'), ('Hamster', 'Hamster'), ('Cat', 'Cat'), ('Gerbil', 'Gerbil')], max_length=30, verbose_name='Type')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Age')),
                ('owner', models.ForeignKey(on_delete=pets.models.Owner, to='pets.Owner')),
            ],
        ),
    ]
