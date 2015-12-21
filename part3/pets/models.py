from __future__ import unicode_literals

from django.db import models
from django.core import validators


class Owner(models.Model):
    """
    A class representing the owner of a pet
    add a to string
    """
    PET_TYPE_CHOICES = {
        ("None", "None"),
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Rabbit", "Rabbit"),
        ("Hamster", "Hamster"),
        ("Gerbil", "Gerbil"),
        ("Bird", "Bird"),
    }

    first_name = models.CharField(
            'First Name',
            max_length=50,
            default=' ',
            validators=[
                validators.RegexValidator(
                        r'^[A-Z][a-zA-Z]*[^_]$',
                        'Name invalid. This value must start with an '
                        'uppercase letter and only contain letters.'
                )
            ]
    )
    last_name = models.CharField(
            'Last Name',
            max_length=50,
            default=' ',
            validators=[
                validators.RegexValidator(
                        r'^[A-Z][a-zA-Z]*[^_]$',
                        'Name invalid. This value must start with an '
                        'uppercase letter and only contain letters.'
                )
            ]
    )
    dob = models.DateField('Date of Birth')
    favorite_pet_type = models.CharField('Favorite Type of Pet', max_length=50, choices=PET_TYPE_CHOICES, blank=True)


def __str__(self):
    return self.first_name + " " + self.last_name


class Pet(models.Model):
    """
    A class representing an animal that is a pet
    """
    PET_TYPE_CHOICES = {
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Rabbit", "Rabbit"),
        ("Hamster", "Hamster"),
        ("Gerbil", "Gerbil"),
        ("Bird", "Bird"),
    }

    name = models.CharField('Name', max_length=50, default=' ')
    type = models.CharField('Type', max_length=30, choices=PET_TYPE_CHOICES)
    owner = models.ForeignKey('Owner', Owner)
    age = models.PositiveIntegerField('Age', default=0)
