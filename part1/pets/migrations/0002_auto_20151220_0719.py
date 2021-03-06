# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='favorite_pet_type',
            field=models.CharField(blank=True, choices=[('Bird', 'Bird'), ('Hamster', 'Hamster'), ('Rabbit', 'Rabbit'), ('Parrot', 'Parrot'), ('Cat', 'Cat'), ('None', 'None'), ('Gerbil', 'Gerbil'), ('Dog', 'Dog')], max_length=50, verbose_name='Favorite Type of Pet'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='first_name',
            field=models.CharField(default=' ', max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='last_name',
            field=models.CharField(default=' ', max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Bird', 'Bird'), ('Hamster', 'Hamster'), ('Rabbit', 'Rabbit'), ('Parrot', 'Parrot'), ('Cat', 'Cat'), ('Gerbil', 'Gerbil'), ('Dog', 'Dog')], max_length=30, verbose_name='Type'),
        ),
    ]
