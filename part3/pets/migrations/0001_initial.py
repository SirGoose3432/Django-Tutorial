# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 19:01
from __future__ import unicode_literals

import django.core.validators
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
                    ('first_name', models.CharField(default=' ', max_length=50, validators=[
                        django.core.validators.RegexValidator('^[A-Z][a-zA-Z]*[^_]$',
                                                              'Name invalid. This value must start with an uppercase letter and only contain letters.')],
                                                    verbose_name='First Name')),
                    ('last_name', models.CharField(default=' ', max_length=50, validators=[
                        django.core.validators.RegexValidator('^[A-Z][a-zA-Z]*[^_]$',
                                                              'Name invalid. This value must start with an uppercase letter and only contain letters.')],
                                                   verbose_name='Last Name')),
                    ('dob', models.DateField(verbose_name='Date of Birth')),
                    ('favorite_pet_type', models.CharField(blank=True, choices=[('Dog', 'Dog'), ('Bird', 'Bird'),
                                                                                ('Rabbit', 'Rabbit'),
                                                                                ('Gerbil', 'Gerbil'), ('None', 'None'),
                                                                                ('Hamster', 'Hamster'),
                                                                                ('Parrot', 'Parrot'), ('Cat', 'Cat')],
                                                           max_length=50, verbose_name='Favorite Type of Pet')),
                ],
        ),
        migrations.CreateModel(
                name='Pet',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('name', models.CharField(default=' ', max_length=50, verbose_name='Name')),
                    ('type', models.CharField(
                        choices=[('Dog', 'Dog'), ('Bird', 'Bird'), ('Rabbit', 'Rabbit'), ('Gerbil', 'Gerbil'),
                                 ('Hamster', 'Hamster'), ('Parrot', 'Parrot'), ('Cat', 'Cat')], max_length=30,
                        verbose_name='Type')),
                    ('age', models.PositiveIntegerField(default=0, verbose_name='Age')),
                    ('owner', models.ForeignKey(on_delete=pets.models.Owner, to='pets.Owner')),
                ],
        ),
    ]
